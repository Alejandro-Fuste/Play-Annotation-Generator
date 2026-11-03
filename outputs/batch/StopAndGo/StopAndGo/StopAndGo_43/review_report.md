# Play-Annotation-Generator Annotation Review — StopAndGo_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 147
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
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `6` | `6` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `6` | `6` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 10 | START | 10 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `13` | `13` | 13 | START | 13 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `14` | 13 | START | 13 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 13 | START | 15 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 13 | START | 13 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 13 | START | 13 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 14 | END | 10 | 14 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `6` | `6` | 29 | START | 29 | 71 |
| ✅ EXACT | `Action_SellStop` | WR1 | `6` | `6` | 72 | START | 72 | 92 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `6` | `6` | 93 | START | 93 | 239 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 111 | START | 111 | 122 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 14 | 5 | inferred_complete_timeline |
| `Action_None` | 15 | 110 | 96 | inferred_complete_timeline |
| `Action_ThrowPass` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_None` | 123 | 152 | 30 | inferred_complete_timeline |
| `Action_None` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 106 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_VerticalStem` | 29 | 71 | 43 | inferred_complete_timeline |
| `Action_SellStop` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_RunGoRoute` | 93 | 239 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 149 | 140 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 66 | 57 | inferred_complete_timeline |
| `Action_None` | 68 | 106 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 122 | 110 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 169 | 157 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 178 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 14 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 56 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 66 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 152 | 140 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 166 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 232 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 52 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 151 | 142 | inferred_complete_timeline |
| `Action_None` | 154 | 160 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 62 | 53 | inferred_complete_timeline |
| `Action_None` | 64 | 105 | 42 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_None` | 128 | 146 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 138 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 115 | 106 | inferred_complete_timeline |
| `Action_None` | 118 | 179 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 131 | 122 | inferred_complete_timeline |
| `Action_None` | 133 | 145 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 107 | 98 | inferred_complete_timeline |
| `Action_None` | 112 | 212 | 101 | inferred_complete_timeline |
| `Action_None` | 216 | 225 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 105 | 96 | inferred_complete_timeline |
| `Action_None` | 108 | 239 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 126 | 117 | inferred_complete_timeline |
| `Action_None` | 130 | 138 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 6–58 | 23 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 72–169 | 28 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 73–75 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 77–118 | 39 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 100–217 | 82 | 9 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 116–160 | 41 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 132–207 | 50 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 138–239 | 59 | 10 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 157–174 | 18 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 162–168 | 6 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 183–239 | 22 | 6 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 192–239 | 33 | 4 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 201–239 | 30 | 4 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 212–235 | 23 | 2 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 218–230 | 9 | 2 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [10–14], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=15.
- ⚠️ Action 'Action_None' range [10-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-105] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-146] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-107] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-212] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-179] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [93-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-126] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-122] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-52] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-106] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-177] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-232] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [111-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-22] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-118] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-126] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-150] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-207] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-220] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-224] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>