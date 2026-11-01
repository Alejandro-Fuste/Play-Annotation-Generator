# Play-Annotation-Generator Annotation Review — InsideZoneRead_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_73`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 4 | START | 4 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 4 | START | 4 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 4 | START | 4 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 4 | START | 4 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 4 | START | 4 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 4 | START | 4 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 4 | START | 4 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `3` | `Group` | 4 | START | 4 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 4 | START | 4 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 4 | START | 4 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 4 | START | 4 | 52 |
| ✅ EXACT | `Action_BallSnap` | C | `3` | `2` | 53 | START | 53 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 55 | START | 55 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 55 | START | 55 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `15` | `14` | 55 | START | 55 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `3` | `2` | 55 | START | 69 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 55 | START | 55 | 123 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 68 | END | 53 | 68 |
| ✅ EXACT | `Action_ReadDefender` | QB | `22` | `21` | 70 | START | 70 | 85 |
| ✅ EXACT | `Action_Handoff` | QB | `22` | `21` | 86 | START | 86 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `20` | `19` | 98 | START | 98 | 229 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 123 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 68 | 16 | inferred_complete_timeline |
| `Action_None` | 69 | 69 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–237
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 97 | 94 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 229 | 132 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–116
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 116 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 237 | 185 | inferred_complete_timeline |
| `Action_None` | 246 | 251 | 6 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 54 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 123 | 69 | inferred_complete_timeline |
| `Action_None` | 134 | 269 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 54 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 69 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 123 | 13 | inferred_complete_timeline |
| `Action_None` | 124 | 146 | 23 | inferred_complete_timeline |
| `Action_None` | 148 | 269 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 53 | 68 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 82 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 123 | 40 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 54 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 81 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 54 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 123 | 69 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 110 | 58 | inferred_complete_timeline |
| `Action_None` | 122 | 138 | 17 | inferred_complete_timeline |
| `Action_None` | 146 | 247 | 102 | inferred_complete_timeline |
| `Action_None` | 249 | 259 | 11 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 239 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 211 | 159 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–246
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 246 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 171 | 119 | inferred_complete_timeline |
| `Action_None` | 176 | 269 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–267
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 267 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 269 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 4–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 52 | 49 | inferred_complete_timeline |
| `Action_None` | 53 | 180 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–113 | 10 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 126–269 | 144 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 156–173 | 14 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 156–158 | 3 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 185–269 | 84 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 259–269 | 9 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [53–68], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=69.
- ⚠️ Action 'Action_None' range [53-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-82] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-267] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [55-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-246] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '29' has 1 frames without a visible bounding box.
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

</details>