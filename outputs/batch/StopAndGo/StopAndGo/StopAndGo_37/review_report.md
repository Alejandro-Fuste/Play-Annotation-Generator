# Play-Annotation-Generator Annotation Review — StopAndGo_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_37`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `6` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `13` | `13` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | LT | `6` | `6` | 8 | START | 8 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 11 | START | 11 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `11` | `11` | 11 | START | 11 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 11 | START | 11 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `6` | 11 | START | 11 | 29 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `20` | `20` | 22 | END | 8 | 20 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `13` | `13` | 22 | START | 22 | 82 |
| ✅ EXACT | `Action_SellStop` | WR1 | `13` | `13` | 83 | START | 83 | 93 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 93 | START | 93 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR1 | `13` | `13` | 94 | START | 94 | 137 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_None` | 27 | 92 | 66 | inferred_complete_timeline |
| `Action_ThrowPass` | 93 | 109 | 17 | inferred_complete_timeline |
| `Action_None` | 110 | 123 | 14 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 58 | 51 | inferred_complete_timeline |
| `Action_None` | 63 | 109 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_VerticalStem` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_SellStop` | 83 | 93 | 11 | inferred_complete_timeline |
| `Action_RunGoRoute` | 94 | 137 | 44 | inferred_complete_timeline |
| `Action_RunGoRoute` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_RunGoRoute` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_RunGoRoute` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_RunGoRoute` | 172 | 179 | 8 | inferred_complete_timeline |
| `Action_RunGoRoute` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_RunGoRoute` | 188 | 190 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 108 | 101 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 64 | 66 | 3 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 10 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 29 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 198 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 216 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 54 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 120 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 143 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 159 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 30 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 269 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 117 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 142 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 20 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 101 | 94 | inferred_complete_timeline |
| `Action_None` | 106 | 125 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 214 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 16 | 9 | inferred_complete_timeline |
| `Action_None` | 18 | 29 | 12 | inferred_complete_timeline |
| `Action_None` | 58 | 95 | 38 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 113 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 220 | 213 | inferred_complete_timeline |
| `Action_None` | 232 | 256 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 225 | 218 | inferred_complete_timeline |
| `Action_None` | 227 | 233 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 257 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 178 | 171 | inferred_complete_timeline |
| `Action_None` | 180 | 193 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 37–269 | 227 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 41–44 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 73–129 | 56 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 86–130 | 23 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 88–98 | 11 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 92–106 | 14 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 127–231 | 52 | 6 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 138–143 | 6 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 144–269 | 126 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 156–179 | 10 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 156–268 | 93 | 4 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 168–269 | 52 | 6 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 172–202 | 31 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 174–261 | 34 | 5 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 182–213 | 6 | 2 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 188–269 | 46 | 5 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 228–262 | 27 | 4 | Undefined position; Undefined team |
| `42` | `66` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 236–269 | 11 | 2 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 249–269 | 11 | 2 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 257–260 | 4 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 260–269 | 10 | 1 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `13` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 103 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [8-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-225] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-46] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-29] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-198] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-216] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-58] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-117] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-101] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [94-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [140-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [148-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [164-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [172-179] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [182-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [188-190] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-269] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-220] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-214] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-95] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [8-20] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-93] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-129] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-106] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-231] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-209] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-202] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-261] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-216] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-240] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-269] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '46' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>