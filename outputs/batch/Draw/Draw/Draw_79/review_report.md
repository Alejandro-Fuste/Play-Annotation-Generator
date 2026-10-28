# Play-Annotation-Generator Annotation Review — Draw_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_79`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 155
- **Validation Warnings:** 143
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 131
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `18` | `17` | 31 | START | 31 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `13` | 34 | START | 34 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `17` | 34 | START | 50 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `2` | `1` | 34 | START | 34 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `19` | 34 | START | 34 | 51 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `20` | 34 | START | 34 | 53 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 49 | END | 31 | 49 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `17` | `16` | 57 | START | 57 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 69 | START | 69 | 97 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 49 | 19 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 69 | 97 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 269 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 98 | 68 | inferred_complete_timeline |
| `Action_None` | 103 | 229 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 74 | 44 | inferred_complete_timeline |
| `Action_None` | 76 | 156 | 81 | inferred_complete_timeline |
| `Action_None` | 158 | 269 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 82 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 82 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 51 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 105 | 46 | inferred_complete_timeline |
| `Action_None` | 106 | 269 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 42 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 78 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 95 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 105 | 1 | inferred_complete_timeline |
| `Action_None` | 106 | 106 | 1 | inferred_complete_timeline |
| `Action_None` | 108 | 117 | 10 | inferred_complete_timeline |
| `Action_None` | 120 | 160 | 41 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 53 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 70 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_None` | 106 | 269 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 85 | 55 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 62 | 32 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 59 | 29 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 95 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 103 | 73 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 147 | 117 | inferred_complete_timeline |
| `Action_None` | 151 | 263 | 113 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 85 | 55 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 100 | 70 | inferred_complete_timeline |
| `Action_None` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 135 | 242 | 108 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 257 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 269 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 142 | 112 | inferred_complete_timeline |
| `Action_None` | 146 | 249 | 104 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 198 | 168 | inferred_complete_timeline |
| `Action_None` | 200 | 269 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 269 | 239 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 17–269 | 248 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 79–140 | 61 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 86–269 | 177 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 101–269 | 150 | 7 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 107–269 | 128 | 10 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 131–269 | 117 | 9 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 138–269 | 87 | 6 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 143–144 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 145–269 | 97 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 146–269 | 60 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 161–260 | 80 | 8 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 182–265 | 40 | 6 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 182–269 | 83 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 211–269 | 59 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 256–269 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 111 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [31–49], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=50.
- ⚠️ Action 'Action_None' range [31-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-229] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-100] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-242] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-156] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-82] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-142] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-249] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-85] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-70] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [69-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [31-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-78] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 106, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [106-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-51] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-140] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-223] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-145] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-246] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-199] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-202] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-179] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-244] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '35' has 2 frames without a visible bounding box.
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

</details>