# Play-Annotation-Generator Annotation Review — OutsideZoneRead_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_97`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | TE2 | offense | `21` | `20` |
| ✅ EXACT | `Action_Keep` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | LG | `20` | `19` | 1 | START | 1 | 3 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 4 | START | 4 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `17` | 4 | START | 4 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 4 | START | 4 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 4 | START | 4 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 4 | START | 5 | 18 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 18 | END | 1 | 18 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `10` | 24 | START | 24 | 34 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | TE2 | `21` | `20` | 30 | START | N/A | N/A |
| ✅ EXACT | `Action_Keep` | QB | `11` | `10` | 35 | START | 35 | 45 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 46 | START | 46 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 70 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 18 | 18 | inferred_complete_timeline |
| `Action_None` | 19 | 23 | 5 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 24 | 34 | 11 | inferred_complete_timeline |
| `Action_Keep` | 35 | 45 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 46 | 269 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 36 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 256 | 218 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 269 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 269 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 97 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 5 | 18 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 67 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 70 | 1 | inferred_complete_timeline |
| `Action_None` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 3 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 11 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 47 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 56 | 57 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 11 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 64 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 11 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 29 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 44 | 70 | 27 | inferred_complete_timeline |
| `Action_None` | 71 | 128 | 58 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_None` | 139 | 269 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 56 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 70 | 13 | inferred_complete_timeline |
| `Action_None` | 71 | 121 | 51 | inferred_complete_timeline |
| `Action_None` | 143 | 154 | 12 | inferred_complete_timeline |
| `Action_None` | 156 | 269 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 269 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 81 | 81 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 93 | 93 | inferred_complete_timeline |
| `Action_None` | 95 | 101 | 7 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 269 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 134 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 129 | 129 | inferred_complete_timeline |
| `Action_None` | 139 | 269 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 109 | 109 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 216 | 71 | inferred_complete_timeline |
| `Action_None` | 219 | 269 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 128 | 128 | inferred_complete_timeline |
| `Action_None` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 93 | 93 | inferred_complete_timeline |
| `Action_None` | 97 | 230 | 134 | inferred_complete_timeline |
| `Action_None` | 232 | 235 | 4 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 136 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 211 | 211 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 156 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 29–269 | 231 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 88–269 | 141 | 8 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 132–269 | 137 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 148–269 | 117 | 6 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 148–269 | 120 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 150–269 | 119 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 164–192 | 21 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 164–269 | 105 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 246–247 | 2 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `21` (TE2)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 76 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [1-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-256] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-230] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-134] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-128] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' for track '10' starts at frame 35, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Keep' range [35-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-11] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [15-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-93] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-109] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-121] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-29] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-128] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [38-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [56-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [5-18] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-36] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-88] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-136] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-197] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-192] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '34' has 3 frames without a visible bounding box.
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

</details>