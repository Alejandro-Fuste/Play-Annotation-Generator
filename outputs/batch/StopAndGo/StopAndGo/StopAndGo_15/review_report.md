# Play-Annotation-Generator Annotation Review — StopAndGo_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_15`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 102
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 15 | START | 15 | 30 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 18 | START | 18 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 18 | START | 18 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 18 | START | 31 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 18 | START | 18 | 89 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 18 | START | 18 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 30 | END | 15 | 30 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 30 | START | 30 | 69 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 70 | START | 70 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `0` | `0` | 88 | START | 88 | 274 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 98 | START | 98 | 110 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 30 | 16 | inferred_complete_timeline |
| `Action_None` | 31 | 97 | 67 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 110 | 13 | inferred_complete_timeline |
| `Action_None` | 111 | 144 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 142 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 159 | 145 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 202 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_VerticalStem` | 30 | 69 | 40 | inferred_complete_timeline |
| `Action_SellStop` | 70 | 87 | 18 | inferred_complete_timeline |
| `Action_RunGoRoute` | 88 | 274 | 187 | inferred_complete_timeline |
| `Action_RunGoRoute` | 285 | 288 | 4 | inferred_complete_timeline |
| `Action_RunGoRoute` | 306 | 310 | 5 | inferred_complete_timeline |
| `Action_RunGoRoute` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 64 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 147 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 111 | 94 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 129 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 152 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 30 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 43 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 153 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 86 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 89 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 149 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 76 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 68 | 54 | inferred_complete_timeline |
| `Action_None` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_None` | 78 | 159 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 173 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 187 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 84 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 170 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 186 | 172 | inferred_complete_timeline |
| `Action_None` | 188 | 253 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 146 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 264 | 250 | inferred_complete_timeline |
| `Action_None` | 267 | 359 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 85 | 71 | inferred_complete_timeline |
| `Action_None` | 89 | 215 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 42–143 | 89 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 72–138 | 54 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 75–156 | 70 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 88–105 | 18 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 104–151 | 29 | 4 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 109–154 | 42 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 114–138 | 5 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 122–153 | 32 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 127–129 | 3 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 140–148 | 7 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 142–146 | 5 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 260–267 | 6 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 288–359 | 72 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 333–342 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [15–30], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_RunGoRoute' range [88-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [285-288] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [306-310] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-159] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-146] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-68] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-142] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-129] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-43] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-153] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-89] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-104] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-93] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-134] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-84] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-96] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-105] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-134] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '36' has 2 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>