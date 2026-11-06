# Play-Annotation-Generator Annotation Review — OutsideZoneRead_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_117`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 3 | START | 3 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 6 | START | 18 | 24 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 6 | START | 6 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 6 | START | 6 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `22` | `21` | 6 | START | 6 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 6 | START | 6 | 34 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 17 | END | 3 | 17 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `11` | 21 | START | 21 | 25 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 26 | START | 26 | 50 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `11` | 51 | START | 51 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 68 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_None` | 18 | 20 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_Keep` | 26 | 50 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 235 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 163 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 246 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 46 | 44 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 96 | 40 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 68 | 63 | inferred_complete_timeline |
| `Action_None` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_None` | 81 | 106 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 68 | 63 | inferred_complete_timeline |
| `Action_None` | 69 | 84 | 16 | inferred_complete_timeline |
| `Action_None` | 87 | 129 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 17 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 68 | 32 | inferred_complete_timeline |
| `Action_None` | 69 | 207 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 28 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 34 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 138 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 255 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 97 | 95 | inferred_complete_timeline |
| `Action_None` | 99 | 194 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 79 | 77 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 193 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 201 | 199 | inferred_complete_timeline |
| `Action_None` | 204 | 208 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 254 | 44 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 193 | 191 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 39–206 | 168 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 46–47 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 49–51 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 55–159 | 89 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 58–77 | 17 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 62–63 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 71–77 | 6 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 80–82 | 3 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 111–209 | 99 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 112–204 | 93 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 125–126 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 127–230 | 101 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 137–269 | 133 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 144–148 | 5 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 148–153 | 6 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 149–186 | 38 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 165–183 | 19 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 167–202 | 28 | 3 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 194–199 | 6 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 213–269 | 53 | 3 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 239–247 | 9 | 1 | Undefined position; Undefined team |
| `43` | `63` | Position_Unknown | Team_Unknown | 247–257 | 11 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [3–17], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=18.
- ⚠️ Action 'Action_None' range [3-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-34] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-138] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-79] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-193] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-193] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-194] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-106] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-84] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-129] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-209] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-204] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-202] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-230] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-148] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-186] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-183] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-185] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-244] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-266] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-247] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-257] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '44' has 1 frames without a visible bounding box.
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

</details>