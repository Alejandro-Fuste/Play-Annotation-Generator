# Play-Annotation-Generator Annotation Review — SplitZone_300

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_300`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `7` | `7` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 83 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 74 | START | 74 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `14` | 84 | START | 84 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 84 | START | 84 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 84 | START | 87 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 84 | START | 84 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 84 | START | 84 | 143 |
| ✅ EXACT | `Action_SnapReceive` | RB | `6` | `6` | 86 | END | 74 | 86 |
| ✅ EXACT | `Action_SplitBlock` | TE | `7` | `7` | 88 | START | 88 | 135 |
| ✅ EXACT | `Action_ReadEdgeDefender` | RB | `6` | `6` | 91 | START | 91 | 101 |
| ✅ EXACT | `Action_PressEdge` | Position_Unknown | `22` | `22` | 92 | START | 92 | 119 |
| ✅ EXACT | `Action_Handoff` | RB | `6` | `6` | 102 | START | 102 | 121 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `22` | 123 | START | 123 | 152 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 102 | 121 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 257 | 136 | inferred_complete_timeline |
| `Action_None` | 262 | 264 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 202 | 129 | inferred_complete_timeline |
| `Action_None` | 204 | 212 | 9 | inferred_complete_timeline |
| `Action_None` | 215 | 269 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_SplitBlock` | 88 | 135 | 48 | inferred_complete_timeline |
| `Action_None` | 136 | 267 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 143 | 60 | inferred_complete_timeline |
| `Action_None` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 99 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 107 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 143 | 20 | inferred_complete_timeline |
| `Action_None` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 86 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 125 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 142 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 161 | 16 | inferred_complete_timeline |
| `Action_None` | 167 | 183 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 112 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 143 | 27 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 216 | 143 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 229 | 269 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 259 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 168 | 95 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 146 | 73 | inferred_complete_timeline |
| `Action_None` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 141 | 68 | inferred_complete_timeline |
| `Action_None` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 251 | 178 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 146 | 73 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 184 | 21 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |
| `Action_None` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 235 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 269 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 241 | 168 | inferred_complete_timeline |
| `Action_None` | 245 | 257 | 13 | inferred_complete_timeline |
| `Action_None` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–152 | 94 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 88–98 | 4 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 165–269 | 104 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 179–224 | 30 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 188–263 | 68 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 231–237 | 4 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 247–268 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [74–86], lower_priority='Action_ZoneBlock' annotated_start=84, effective_Action_ZoneBlock_start=87.
- ⚠️ Action 'Action_None' range [74-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-241] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-146] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-267] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [109-112] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-143] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-269] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-184] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-112] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-216] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [92-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [123-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-212] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-268] for track '28' has 2 frames without a visible bounding box.
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

</details>