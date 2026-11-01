# Play-Annotation-Generator Annotation Review — InsideZoneRead_25

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_25`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 5 | START | 5 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 5 | START | 5 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 5 | START | 5 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 5 | START | 5 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 5 | START | 5 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 5 | START | 5 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 5 | START | 5 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 5 | START | 5 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 5 | START | 5 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 5 | START | 5 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 5 | START | 5 | 141 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 142 | START | 142 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 144 | START | 159 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 144 | START | 144 | 165 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `16` | 144 | START | 144 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 144 | START | 144 | 207 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 144 | START | 144 | 221 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 158 | END | 142 | 158 |
| ✅ EXACT | `Action_ReadDefender` | QB | `9` | `8` | 161 | START | 161 | 173 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 174 | START | 174 | 183 |
| ✅ EXACT | `Action_BallCarry` | RB | `18` | `17` | 184 | START | 184 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 221 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 5–263
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_SnapReceive` | 142 | 158 | 17 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 183 | 10 | inferred_complete_timeline |
| `Action_None` | 184 | 263 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 169 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 184 | 269 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–267
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 198 | 57 | inferred_complete_timeline |
| `Action_None` | 206 | 264 | 59 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–242
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 143 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 207 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 221 | 1 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 237 | 10 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 143 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 221 | 78 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_BallSnap` | 142 | 158 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 212 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 221 | 7 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 143 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 165 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 182 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 221 | 36 | inferred_complete_timeline |
| `Action_None` | 222 | 236 | 15 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 269 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 143 | 139 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 221 | 78 | inferred_complete_timeline |
| `Action_None` | 222 | 225 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 269 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 234 | 93 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 245 | 264 | 20 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–181
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 162 | 21 | inferred_complete_timeline |
| `Action_None` | 178 | 181 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–199
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 199 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 5–206
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 206 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 141 | 137 | inferred_complete_timeline |
| `Action_None` | 142 | 269 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 5–264 | 234 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 12–16 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 159–269 | 88 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–262 | 65 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 202–269 | 61 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [142–158], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=159.
- ⚠️ Action 'Action_None' range [142-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-264] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-264] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-212] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-182] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-236] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-169] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [211-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-178] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-211] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-224] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-262] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>