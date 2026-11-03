# Play-Annotation-Generator Annotation Review — StopAndGo_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_23`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_VerticalStem` | WR4 | offense | `6` | `6` |
| ✅ EXACT | `Action_SellStop` | WR4 | offense | `6` | `6` |
| ✅ EXACT | `Action_PumpFake` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR4 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 20 | START | 20 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 23 | START | 23 | 63 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `15` | `15` | 23 | START | 37 | 45 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 23 | START | 23 | 129 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 23 | START | 23 | 133 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 23 | START | 23 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 36 | END | 20 | 36 |
| ✅ EXACT | `Action_VerticalStem` | WR4 | `6` | `6` | 36 | START | 36 | 52 |
| ✅ EXACT | `Action_SellStop` | WR4 | `6` | `6` | 53 | START | 53 | 81 |
| ✅ EXACT | `Action_PumpFake` | QB | `16` | `16` | 55 | START | 55 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR4 | `6` | `6` | 82 | START | 82 | 238 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 105 | START | 105 | 114 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_None` | 37 | 54 | 18 | inferred_complete_timeline |
| `Action_PumpFake` | 55 | 80 | 26 | inferred_complete_timeline |
| `Action_None` | 81 | 104 | 24 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 114 | 10 | inferred_complete_timeline |
| `Action_None` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 173 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 93 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 178 | 159 | inferred_complete_timeline |
| `Action_None` | 220 | 233 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 218 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_VerticalStem` | 36 | 52 | 17 | inferred_complete_timeline |
| `Action_SellStop` | 53 | 81 | 29 | inferred_complete_timeline |
| `Action_RunGoRoute` | 82 | 238 | 157 | inferred_complete_timeline |
| `Action_RunGoRoute` | 241 | 322 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 129 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 133 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 45 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 157 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 63 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 132 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 69 | 50 | inferred_complete_timeline |
| `Action_None` | 72 | 124 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 97 | 78 | inferred_complete_timeline |
| `Action_None` | 103 | 135 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 110 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 179 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 171 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 116 | 97 | inferred_complete_timeline |
| `Action_None` | 119 | 130 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 179 | 160 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 218 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 220 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 143 | 124 | inferred_complete_timeline |
| `Action_None` | 147 | 218 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 203 | 184 | inferred_complete_timeline |
| `Action_None` | 205 | 218 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 201 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–154 | 102 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 83–91 | 5 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 121–137 | 17 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 121–145 | 25 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 185–187 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 189–218 | 30 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 209–218 | 10 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 210–218 | 9 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 219–241 | 23 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 219–259 | 29 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 219–329 | 111 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 221–229 | 9 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 221–233 | 13 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 221–226 | 6 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 234–237 | 4 | 1 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 245–329 | 85 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `15` (C): Annotated start 23 != Inferred start 37
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [20–36], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=37.
- ⚠️ Action 'Action_None' range [20-69] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-124] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-218] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-143] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-218] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [82-238] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [241-322] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-218] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-130] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-133] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-157] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-145] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-218] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-233] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '42' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>