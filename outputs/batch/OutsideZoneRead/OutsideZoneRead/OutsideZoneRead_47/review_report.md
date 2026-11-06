# Play-Annotation-Generator Annotation Review — OutsideZoneRead_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_47`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 60
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 203
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `10` | 73 | START | 73 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 73 | START | 73 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `18` | 73 | START | 73 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 73 | START | 73 | 80 |
| ✅ EXACT | `Action_PressEdge` | RB | `16` | `16` | 76 | START | 76 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | QB | `13` | `13` | 84 | START | 84 | 92 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `13` | `13` | 100 | START | 103 | 107 |

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
- **Visible Frames:** 0–261
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 84 | 92 | 9 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 183 | 76 | inferred_complete_timeline |
| `Action_None` | 185 | 261 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PressEdge` | 76 | 98 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 139 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 121 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 156 | 29 | inferred_complete_timeline |
| `Action_None` | 157 | 319 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 127 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 134 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 172 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 88 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 156 | 14 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 165 | 253 | 89 | inferred_complete_timeline |
| `Action_None` | 256 | 276 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 121 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 143 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 158 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 283 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 110 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 186 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 254 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 277 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 295 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–242 | 243 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 28–81 | 54 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 82–233 | 79 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 97–147 | 45 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 106–108 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 137–158 | 22 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 141–258 | 116 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 154–260 | 106 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 159–188 | 19 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 162–479 | 297 | 7 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 166–242 | 77 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 167–298 | 126 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 171–279 | 106 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 176–330 | 152 | 3 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 182–270 | 72 | 4 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 196–249 | 54 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 197–205 | 8 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 218–305 | 88 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 220–479 | 245 | 5 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 224–365 | 142 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 247–299 | 53 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 267–460 | 188 | 3 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 280–288 | 9 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 282–321 | 20 | 6 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 335–479 | 140 | 2 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 375–464 | 88 | 2 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 380–479 | 100 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 384–404 | 7 | 3 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 409–411 | 3 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 413–423 | 11 | 1 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 419–423 | 5 | 1 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 444–479 | 36 | 1 | Undefined position; Undefined team |
| `53` | `82` | Position_Unknown | Team_Unknown | 455–479 | 25 | 1 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 459–479 | 7 | 2 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 462–463 | 2 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 467–468 | 2 | 1 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 473–474 | 2 | 1 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ReadEdgeDefender` and target `13` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `13` (QB): Annotated start 100 != Inferred start 103

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 121 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 96: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-277] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-295] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-254] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-253] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-276] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-162] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-158] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [84-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [94-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-183] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-261] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-127] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-134] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [76-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-88] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-233] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-144] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-250] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-184] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-377] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-441] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-464] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-469] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-242] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-187] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-298] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-279] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-188] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-222] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-330] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-191] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-209] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-270] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-202] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-305] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-314] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-321] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-343] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-353] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-479] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-365] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-299] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-433] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-444] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-460] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-288] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-285] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-300] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-305] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-337] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-479] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-459] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-464] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-479] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-386] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-404] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-411] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-423] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-423] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-463] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-479] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-463] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-468] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-474] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-479] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.

</details>