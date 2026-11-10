# Play-Annotation-Generator Annotation Review — RPO_83

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_83`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `40` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 34 | START | 34 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 34 | START | 34 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 34 | START | 34 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 34 | START | 34 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `9` | 34 | START | 34 | 75 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `11` | 44 | START | 44 | 53 |
| ✅ EXACT | `Action_PullBall` | QB | `11` | `11` | 54 | START | 54 | 62 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 91 | START | 91 | 98 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 43 | 11 | inferred_complete_timeline |
| `Action_ReadDefender` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 54 | 62 | 9 | inferred_complete_timeline |
| `Action_None` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_ThrowPass` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 104 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 44 | 12 | inferred_complete_timeline |
| `Action_None` | 60 | 75 | 16 | inferred_complete_timeline |
| `Action_None` | 77 | 104 | 28 | inferred_complete_timeline |
| `Action_None` | 106 | 140 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–36
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 75 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 91 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 83 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 98 | 10 | inferred_complete_timeline |
| `Action_None` | 99 | 111 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 60 | 7 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 98 | 65 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 98 | 65 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 69 | 37 | inferred_complete_timeline |
| `Action_None` | 72 | 106 | 35 | inferred_complete_timeline |
| `Action_None` | 111 | 128 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 99 | 67 | inferred_complete_timeline |
| `Action_None` | 104 | 114 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 88 | 56 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 104 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 104 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_None` | 33 | 104 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 40–47 | 8 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 47–54 | 8 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 50–104 | 55 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 56–72 | 16 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 74–117 | 40 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 74–106 | 20 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 81–104 | 24 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 81–96 | 16 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–106 | 17 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 105–121 | 12 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 105–111 | 7 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 105–111 | 6 | 2 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 107–111 | 5 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 107–111 | 5 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 107–111 | 5 | 1 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 107–116 | 10 | 1 | Undefined position; Undefined team |
| `35` | `36` | Position_Unknown | Team_Unknown | 107–109 | 3 | 1 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 112–180 | 69 | 1 | Undefined position; Undefined team |
| `37` | `38` | Position_Unknown | Team_Unknown | 112–116 | 5 | 1 | Undefined position; Undefined team |
| `38` | `39` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `39` | `40` | Position_Unknown | Team_Unknown | 116–163 | 45 | 2 | Undefined position; Undefined team |
| `40` | `43` | Position_Unknown | Team_Unknown | 118–177 | 60 | 1 | Undefined position; Undefined team |
| `41` | `44` | Position_Unknown | Team_Unknown | 118–121 | 4 | 1 | Undefined position; Undefined team |
| `42` | `45` | Position_Unknown | Team_Unknown | 118–121 | 4 | 1 | Undefined position; Undefined team |
| `43` | `46` | Position_Unknown | Team_Unknown | 122–146 | 25 | 1 | Undefined position; Undefined team |
| `44` | `47` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `45` | `48` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `46` | `50` | Position_Unknown | Team_Unknown | 151–154 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [33-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-104] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-104] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-91] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-60] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-89] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-106] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-111] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-163] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-177] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-146] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>