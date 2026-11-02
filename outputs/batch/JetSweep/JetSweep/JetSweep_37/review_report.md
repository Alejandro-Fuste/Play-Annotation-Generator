# Play-Annotation-Generator Annotation Review — JetSweep_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_37`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 114
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 27
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `3` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `3` | `2` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `14` | `13` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_JetMotion` | WR | `3` | `2` | 25 | START | 25 | 201 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 56 | START | 56 | 67 |
| ✅ EXACT | `Action_LeadBlock` | TE | `10` | `9` | 58 | START | 58 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 58 | START | 58 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 58 | START | 68 | 92 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 58 | START | 58 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 58 | START | 58 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 58 | START | 58 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 67 | END | 56 | 67 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 74 | START | 74 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `16` | `15` | 77 | START | 79 | 212 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `12` | `11` | 83 | START | 83 | 104 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `12` | `11` | 104 | BOUNDARY | 83 | 104 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `14` | `13` | 104 | BOUNDARY | 58 | 104 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `14` | `13` | 104 | BOUNDARY | 58 | 104 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `17` | `16` | 104 | BOUNDARY | 95 | 104 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `18` | `17` | 104 | BOUNDARY | 89 | 104 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_Toss` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 212 | 134 | inferred_complete_timeline |
| `Action_BallCarry` | 215 | 290 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_JetMotion` | 25 | 201 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 84 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_LeadBlock` | 58 | 104 | 47 | inferred_complete_timeline |
| `Action_None` | 105 | 123 | 19 | inferred_complete_timeline |
| `Action_None` | 125 | 308 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 104 | 47 | inferred_complete_timeline |
| `Action_None` | 105 | 252 | 148 | inferred_complete_timeline |
| `Action_None` | 255 | 260 | 6 | inferred_complete_timeline |
| `Action_None` | 270 | 277 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 78 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 83 | 104 | 22 | inferred_complete_timeline |
| `Action_None` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BallSnap` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 92 | 25 | inferred_complete_timeline |
| `Action_None` | 115 | 125 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 87 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_None` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 75 | 81 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 104 | 16 | inferred_complete_timeline |
| `Action_None` | 105 | 329 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 77 | 22 | inferred_complete_timeline |
| `Action_None` | 83 | 158 | 76 | inferred_complete_timeline |
| `Action_None` | 169 | 213 | 45 | inferred_complete_timeline |
| `Action_None` | 217 | 223 | 7 | inferred_complete_timeline |
| `Action_None` | 234 | 272 | 39 | inferred_complete_timeline |
| `Action_None` | 280 | 297 | 18 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 320 | 6 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 24–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 55 | 32 | inferred_complete_timeline |
| `Action_None` | 56 | 56 | 1 | inferred_complete_timeline |
| `Action_None` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_None` | 68 | 329 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 329 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 112 | 57 | inferred_complete_timeline |
| `Action_None` | 119 | 329 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 133 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 100 | 45 | inferred_complete_timeline |
| `Action_None` | 106 | 113 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 182 | 127 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–329 | 318 | 5 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–329 | 328 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 69–329 | 259 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 108–329 | 218 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 111–127 | 17 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 111–329 | 219 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 122–329 | 208 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 134–227 | 89 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 148–150 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 149–154 | 5 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 149–329 | 170 | 6 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 166–329 | 159 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 194–329 | 133 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 214–263 | 31 | 4 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 222–329 | 108 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 239–241 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 256–329 | 71 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 300–329 | 30 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 321–322 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 22 | 54 | 16 | 48.5% | 25–26, 28–42 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [56–67], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=68.
- ⚠️ Action 'Action_None' range [56-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-113] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [25-201] for track '2' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-173] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-308] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-329] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-252] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-277] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-213] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-272] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-297] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [74-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [215-290] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-87] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-66] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [75-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 56, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [56-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-274] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-155] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-329] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-215] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-248] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-281] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-310] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-329] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-267] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-290] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>