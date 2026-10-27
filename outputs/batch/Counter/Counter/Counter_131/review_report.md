# Play-Annotation-Generator Annotation Review — Counter_131

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_131`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 103
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
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `24` | `22` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `9` | `7` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `23` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `12` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `16` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 36 | START | 36 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 36 | START | 36 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 36 | START | 36 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 36 | START | 36 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 36 | START | 36 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 36 | START | 36 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 36 | START | 36 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 36 | START | 36 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 36 | START | 36 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 36 | START | 36 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 36 | START | 36 | 104 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `15` | 100 | START | 100 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `15` | 105 | START | 117 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `24` | `22` | 105 | START | 105 | 158 |
| ✅ EXACT | `Action_DownBlock` | LT | `9` | `7` | 105 | START | 105 | 185 |
| ✅ EXACT | `Action_PullBlock` | RG | `23` | `21` | 105 | START | 105 | 208 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `12` | `10` | 105 | START | 105 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `16` | `14` | 107 | START | 107 | 141 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `12` | 116 | END | 100 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `12` | 142 | START | 142 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `14` | 155 | START | 155 | 223 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 36–185
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 117 | 141 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 142 | 154 | 13 | inferred_complete_timeline |
| `Action_None` | 155 | 185 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 106 | 71 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 107 | 141 | 35 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 223 | 69 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 182 | 83 | inferred_complete_timeline |
| `Action_None` | 184 | 269 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 36–163
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 104 | 69 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 105 | 163 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 104 | 69 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 185 | 81 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 36–200
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 104 | 69 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 158 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 200 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 36–260
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 178 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 208 | 16 | inferred_complete_timeline |
| `Action_None` | 209 | 247 | 39 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 104 | 69 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 208 | 104 | inferred_complete_timeline |
| `Action_None` | 209 | 269 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 36–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 120 | 133 | 14 | inferred_complete_timeline |
| `Action_None` | 135 | 221 | 87 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 36–187
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 182 | 83 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 36–203
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 198 | 99 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 36–136
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 136 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 36–243
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 240 | 141 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 36–269
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 198 | 99 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 36–269
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 187 | 88 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 36–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 36–269
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 132 | 33 | inferred_complete_timeline |
| `Action_None` | 136 | 219 | 84 | inferred_complete_timeline |
| `Action_None` | 221 | 269 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 36–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 36–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 100 | 269 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `15` | Position_Unknown | Team_Unknown | 36–269 | 234 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 111–119 | 9 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 136–223 | 87 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 143–218 | 38 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 149–154 | 6 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 176–196 | 10 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 178–269 | 71 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 208–269 | 58 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 210–269 | 51 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 224–269 | 22 | 8 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 232–246 | 14 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 236–269 | 34 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 242–269 | 21 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 264: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (LT) duration 104 frames exceeds threshold 90 frames [start=105, end=208].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (C) duration 104 frames exceeds threshold 90 frames [start=105, end=208].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [100–116], lower_priority='Action_DownBlock' annotated_start=105, effective_Action_DownBlock_start=117.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 104 frames exceeds threshold 90 frames [start=105, end=208].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '22' (LG) duration 96 frames exceeds threshold 90 frames [start=105, end=200].
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-219] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [105-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [107-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-191] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-198] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-221] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [160-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-191] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-249] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-235] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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