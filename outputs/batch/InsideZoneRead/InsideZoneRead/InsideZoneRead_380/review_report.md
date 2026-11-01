# Play-Annotation-Generator Annotation Review — InsideZoneRead_380

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_380`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `6` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 3 | START | 3 | 19 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 6 | START | 20 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 6 | START | 6 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 6 | START | 6 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 6 | START | 6 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `8` | 6 | START | 6 | 81 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 19 | END | 3 | 19 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `9` | 23 | START | 23 | 31 |
| ✅ EXACT | `Action_Keep` | QB | `10` | `9` | 32 | START | 32 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `10` | `9` | 52 | START | 52 | 225 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 23 | 31 | 9 | inferred_complete_timeline |
| `Action_Keep` | 32 | 51 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 225 | 174 | inferred_complete_timeline |
| `Action_BallCarry` | 228 | 234 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 239 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 241 | 243 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 245 | 269 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 44 | 42 | inferred_complete_timeline |
| `Action_None` | 47 | 76 | 30 | inferred_complete_timeline |
| `Action_None` | 78 | 88 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 247 | 150 | inferred_complete_timeline |
| `Action_None` | 249 | 250 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 201 | 199 | inferred_complete_timeline |
| `Action_None` | 203 | 253 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 114 | 112 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 43 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 81 | 76 | inferred_complete_timeline |
| `Action_None` | 82 | 107 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 81 | 62 | inferred_complete_timeline |
| `Action_None` | 82 | 135 | 54 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 73 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 81 | 76 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 106 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 44 | 132 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 269 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 4 | 2 | inferred_complete_timeline |
| `Action_None` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_None` | 23 | 60 | 38 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 76 | 246 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 11 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 81 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 132 | 130 | inferred_complete_timeline |
| `Action_None` | 138 | 158 | 21 | inferred_complete_timeline |
| `Action_None` | 161 | 204 | 44 | inferred_complete_timeline |
| `Action_None` | 206 | 223 | 18 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 248 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 100 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 123 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 35–38 | 4 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 65–121 | 57 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 66–249 | 152 | 9 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 74–85 | 11 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 98–257 | 138 | 9 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 98–255 | 114 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 111–254 | 137 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 111–249 | 139 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 115–269 | 127 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 120–124 | 4 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 122–251 | 118 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 124–269 | 74 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 142–244 | 81 | 5 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 143–186 | 43 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 164–172 | 5 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 184–260 | 75 | 3 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 191–204 | 13 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 203–206 | 4 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 207–259 | 20 | 3 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 209–256 | 43 | 2 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 248–250 | 3 | 1 | Undefined position; Undefined team |
| `43` | `74` | Position_Unknown | Team_Unknown | 252–269 | 17 | 2 | Undefined position; Undefined team |
| `44` | `85` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |
| `45` | `87` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 6 != Inferred start 20
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (5 segments found)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 111 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=20.
- ⚠️ Action 'Action_None' range [3-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-223] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-201] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-44] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-88] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [228-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-4] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-60] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-246] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-121] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-92] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-205] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-225] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-181] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-225] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-246] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-249] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-201] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-183] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-246] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-204] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-259] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-228] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-256] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-265] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-269] for track '44' has 1 frames without a visible bounding box.
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

</details>