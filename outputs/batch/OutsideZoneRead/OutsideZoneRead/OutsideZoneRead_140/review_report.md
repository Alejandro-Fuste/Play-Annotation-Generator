# Play-Annotation-Generator Annotation Review — OutsideZoneRead_140

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_140`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 2 | START | 2 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 5 | START | 5 | 29 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `10` | `9` | 5 | START | 5 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 5 | START | 20 | 21 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `13` | 5 | START | 5 | 16 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 5 | START | 5 | 75 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `14` | `13` | 17 | START | 17 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 19 | END | 2 | 19 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `15` | `14` | 21 | START | 21 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `15` | `14` | 26 | START | 26 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `15` | `14` | 46 | START | 46 | 56 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 75 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 2 | 19 | 18 | inferred_complete_timeline |
| `Action_None` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 21 | 25 | 5 | inferred_complete_timeline |
| `Action_Keep` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_Keep` | 41 | 45 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 152 | 95 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 195 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 39 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 35 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 75 | 71 | inferred_complete_timeline |
| `Action_None` | 76 | 190 | 115 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 61 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 19 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 75 | 49 | inferred_complete_timeline |
| `Action_None` | 76 | 89 | 14 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 17 | 75 | 59 | inferred_complete_timeline |
| `Action_None` | 76 | 146 | 71 | inferred_complete_timeline |
| `Action_None` | 148 | 194 | 47 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 29 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 33 | 43 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 46 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 73 | 72 | inferred_complete_timeline |
| `Action_None` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 173 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 106 | 105 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 210 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 76 | 75 | inferred_complete_timeline |
| `Action_None` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 81 | 80 | inferred_complete_timeline |
| `Action_None` | 84 | 106 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 40–204 | 145 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 42–110 | 69 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 50–101 | 52 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 52–97 | 46 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 54–209 | 146 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 59–91 | 33 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 60–110 | 51 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 64–87 | 24 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 66–210 | 145 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 85–210 | 120 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 92–210 | 119 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 92–93 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 100–210 | 111 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 133–210 | 77 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 159–200 | 41 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 186–210 | 25 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 197–201 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [2–19], lower_priority='Action_ZoneBlock' annotated_start=5, effective_Action_ZoneBlock_start=20.
- ⚠️ Action 'Action_ZoneBlock' range [5-29] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [33-43] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-75] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-76] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-81] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-46] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-39] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-173] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-35] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-194] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [26-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [46-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [200-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-101] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-97] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-110] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-187] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-196] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>