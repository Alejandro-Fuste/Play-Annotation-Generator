# Play-Annotation-Generator Annotation Review — RPO_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_55`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `0` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_ReadDefender` | QB | `16` | `16` | 42 | START | 42 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 42 | START | 42 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 42 | START | 42 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | C | `20` | `20` | 42 | START | 42 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 42 | START | 42 | 42 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 42 | START | 42 | 86 |
| ✅ EXACT | `Action_PullBall` | QB | `16` | `16` | 50 | START | 50 | 58 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 77 | START | 77 | 86 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 42 | 49 | 8 | inferred_complete_timeline |
| `Action_PullBall` | 50 | 58 | 9 | inferred_complete_timeline |
| `Action_None` | 59 | 76 | 18 | inferred_complete_timeline |
| `Action_ThrowPass` | 77 | 86 | 10 | inferred_complete_timeline |
| `Action_None` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 176 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 64 | 24 | inferred_complete_timeline |
| `Action_None` | 67 | 107 | 41 | inferred_complete_timeline |
| `Action_None` | 115 | 152 | 38 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 61 | 21 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 87 | 104 | 18 | inferred_complete_timeline |
| `Action_None` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_None` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 87 | 87 | 1 | inferred_complete_timeline |
| `Action_None` | 106 | 166 | 61 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 87 | 109 | 23 | inferred_complete_timeline |
| `Action_None` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_None` | 125 | 178 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 42 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_None` | 87 | 165 | 79 | inferred_complete_timeline |
| `Action_None` | 168 | 176 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 73 | 33 | inferred_complete_timeline |
| `Action_None` | 75 | 85 | 11 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 102 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 87 | 47 | inferred_complete_timeline |
| `Action_None` | 114 | 120 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 128 | 88 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 74 | 34 | inferred_complete_timeline |
| `Action_None` | 77 | 125 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–149 | 150 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 45–50 | 6 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 65–96 | 31 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 82–165 | 45 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 94–127 | 8 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 101–180 | 63 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 102–104 | 3 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 117–174 | 40 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 126–180 | 55 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 126–129 | 4 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 129–180 | 52 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 129–131 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 132–180 | 47 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 137–179 | 14 | 5 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 156–176 | 21 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [41-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-74] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-125] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-176] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-107] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-152] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-102] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-86] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 87, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [87-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-166] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-104] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-132] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-109] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-178] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '21' starts at frame 42, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [42-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-88] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-165] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-180] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-174] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-176] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>