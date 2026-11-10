# Play-Annotation-Generator Annotation Review — RPO_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_62`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `25` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_ReadDefender` | QB | `13` | `13` | 59 | START | 59 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `0` | `0` | 60 | START | 60 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 60 | START | 60 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 60 | START | 60 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `7` | 60 | START | 60 | 106 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 60 | START | 60 | 122 |
| ✅ EXACT | `Action_PullBall` | QB | `13` | `13` | 73 | START | 73 | 92 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 108 | START | 108 | 122 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_ReadDefender` | 59 | 72 | 14 | inferred_complete_timeline |
| `Action_PullBall` | 73 | 92 | 20 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 122 | 15 | inferred_complete_timeline |
| `Action_None` | 123 | 197 | 75 | inferred_complete_timeline |
| `Action_None` | 199 | 207 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 82 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 98 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 122 | 63 | inferred_complete_timeline |
| `Action_None` | 123 | 137 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 122 | 63 | inferred_complete_timeline |
| `Action_None` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_None` | 159 | 171 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 94 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 122 | 21 | inferred_complete_timeline |
| `Action_None` | 123 | 158 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 106 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 119 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 153 | 31 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 122 | 63 | inferred_complete_timeline |
| `Action_None` | 123 | 210 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 75 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 210 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 63 | 156 | 94 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_None` | 88 | 98 | 11 | inferred_complete_timeline |
| `Action_None` | 100 | 166 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 84 | 26 | inferred_complete_timeline |
| `Action_None` | 86 | 115 | 30 | inferred_complete_timeline |
| `Action_None` | 127 | 145 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 70 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 145 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 145 | 87 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 13–117 | 69 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 76–210 | 119 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 91–210 | 113 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 93–106 | 13 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 102–210 | 107 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 105–106 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 113–137 | 25 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 131–138 | 8 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 134–210 | 77 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 143–210 | 68 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 150–210 | 61 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 173–210 | 38 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 182–194 | 13 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 57 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [123-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-75] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-82] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-153] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-137] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-86] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [73-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-197] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-131] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-147] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '31' has 1 frames without a visible bounding box.
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

</details>