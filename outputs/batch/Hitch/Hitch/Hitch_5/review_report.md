# Play-Annotation-Generator Annotation Review — Hitch_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_5`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 45
- **Ball Tracks:** 1
- **Action Segments:** 100
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR1 | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR1 | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 5 | START | 5 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `10` | `10` | 8 | START | 8 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 8 | START | 8 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 8 | START | 22 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 8 | START | 8 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `4` | `4` | 8 | START | 8 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunHitchRoute` | WR1 | `13` | `13` | 21 | START | 21 | 99 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 21 | END | 5 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 79 | START | 79 | 85 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | WR1 | `13` | `13` | 136 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 21 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 78 | 57 | inferred_complete_timeline |
| `Action_ThrowPass` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 133 | 22 | inferred_complete_timeline |
| `Action_None` | 161 | 190 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 32 | 28 | inferred_complete_timeline |
| `Action_None` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_None` | 50 | 68 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 21 | 99 | 79 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 107 | 112 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 112 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 78 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 93 | 86 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 213 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 106 | 99 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 211 | 100 | inferred_complete_timeline |
| `Action_PassBlock` | 213 | 226 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 232 | 235 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 21 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 120 | 99 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 133 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 130 | 123 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 204 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 48 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 55 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 96 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 195 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 197 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 116 | 112 | inferred_complete_timeline |
| `Action_None` | 122 | 124 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 75 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 96 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 114 | 110 | inferred_complete_timeline |
| `Action_None` | 127 | 143 | 17 | inferred_complete_timeline |
| `Action_None` | 148 | 188 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 138 | 134 | inferred_complete_timeline |
| `Action_None` | 151 | 180 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 67 | 63 | inferred_complete_timeline |
| `Action_None` | 73 | 115 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 41 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 23–329 | 305 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 53–58 | 6 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 96–99 | 4 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 111–173 | 63 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 114–329 | 216 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 125–250 | 124 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 140–329 | 179 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 161–173 | 13 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 174–238 | 65 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 180–329 | 150 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 181–236 | 56 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 203–208 | 4 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 217–221 | 5 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 249–329 | 80 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 252–329 | 78 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 253–258 | 6 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 260–329 | 70 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 265–289 | 25 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 269–329 | 61 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 275–286 | 12 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 293–298 | 6 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 297–301 | 5 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 315–329 | 15 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `38` | 214 | 214 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunHitchRoute` and target `13` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `13` (WR1)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '13' has invalid range: start=136, end=112. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [5–21], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=22.
- ⚠️ Action 'Action_None' range [5-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-41] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-115] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [213-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [232-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [79-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-32] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [160-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-96] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [21-99] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunHitchRoute' range [107-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-133] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-138] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-213] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-214] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-270] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-319] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-238] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-327] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-289] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-298] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '45' has 1 frames without a visible bounding box.
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