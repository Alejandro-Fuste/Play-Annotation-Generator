# Play-Annotation-Generator Annotation Review — OutsideZoneRead_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_4`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 76 | START | 76 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 76 | START | 76 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 76 | START | 76 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | C | `6` | `6` | 76 | START | 76 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `8` | 76 | START | 76 | 80 |
| ✅ EXACT | `Action_PressEdge` | QB | `7` | `7` | 78 | START | 78 | 97 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 98 | START | 98 | 99 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `2` | `2` | 98 | START | 98 | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PressEdge` | 78 | 97 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 107 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 173 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 276 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 22 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 75 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 100 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_None` | 123 | 251 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 122 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 128 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 143 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 122 | 47 | inferred_complete_timeline |
| `Action_None` | 123 | 123 | 1 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 179 | 43 | inferred_complete_timeline |
| `Action_None` | 186 | 203 | 18 | inferred_complete_timeline |
| `Action_None` | 205 | 221 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 122 | 35 | inferred_complete_timeline |
| `Action_None` | 123 | 149 | 27 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 87 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 119 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 154 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 160 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 180 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 202 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 279 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 329 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 171 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 183 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 216 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 52–170 | 104 | 6 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 55–118 | 64 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 55–95 | 41 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 85–233 | 97 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 91–244 | 132 | 8 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 139–326 | 186 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 144–174 | 31 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 148–329 | 165 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 175–329 | 154 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 183–202 | 13 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 195–198 | 4 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 195–226 | 32 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 202–218 | 13 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 205–329 | 117 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 210–229 | 20 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 218–329 | 112 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 222–240 | 19 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 305–329 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 84 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-202] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-279] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 123, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [123-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-179] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-221] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [78-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [98-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-183] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-276] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-282] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-329] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-75] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-138] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-95] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-282] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-326] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-193] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-208] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-202] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-198] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-207] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-305] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-240] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-301] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>