# Play-Annotation-Generator Annotation Review — RPO_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_82`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `24` | source `Route` | no temporal frame

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
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `0` | `0` | 74 | START | 74 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `11` | `11` | 74 | START | 74 | 139 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `14` | 74 | START | 74 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 74 | START | 74 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `9` | 74 | START | 74 | 139 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `10` | 81 | START | 81 | 90 |
| ✅ EXACT | `Action_PullBall` | QB | `10` | `10` | 91 | START | 91 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `10` | `10` | 135 | START | 135 | 135 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 81 | 90 | 10 | inferred_complete_timeline |
| `Action_PullBall` | 91 | 113 | 23 | inferred_complete_timeline |
| `Action_None` | 115 | 131 | 17 | inferred_complete_timeline |
| `Action_None` | 134 | 134 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 135 | 135 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 163 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 156 | 84 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 111 | 39 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 61 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 139 | 47 | inferred_complete_timeline |
| `Action_None` | 140 | 158 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 139 | 66 | inferred_complete_timeline |
| `Action_None` | 140 | 156 | 17 | inferred_complete_timeline |
| `Action_None` | 158 | 166 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 139 | 66 | inferred_complete_timeline |
| `Action_None` | 140 | 167 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 139 | 66 | inferred_complete_timeline |
| `Action_None` | 140 | 177 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 139 | 53 | inferred_complete_timeline |
| `Action_None` | 140 | 187 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 168 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 88 | 151 | 64 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 156 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 171 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |
| `Action_None` | 136 | 152 | 17 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 170 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 72 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 173 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_None` | 83 | 187 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 110–156 | 47 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 120–124 | 5 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 157–168 | 11 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 167–191 | 25 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 169–359 | 191 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 180–181 | 2 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 189–234 | 27 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 204–359 | 156 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 210–255 | 22 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 211–290 | 26 | 6 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 220–257 | 38 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 227–244 | 7 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 233–304 | 51 | 6 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 257–283 | 19 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 262–301 | 13 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 273–306 | 21 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 278–290 | 12 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 285–338 | 13 | 3 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 325–343 | 19 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 351–352 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 87 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [74-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [90-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-173] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-152] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-156] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-168] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-167] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [91-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' for track '10' starts at frame 135, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ThrowPass' range [135-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-156] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-61] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-151] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-191] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-234] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-257] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-261] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-283] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-283] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-284] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-343] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '38' has 1 frames without a visible bounding box.
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

</details>