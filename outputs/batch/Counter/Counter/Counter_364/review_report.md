# Play-Annotation-Generator Annotation Review — Counter_364

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_364`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 144 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 144 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `18` | `17` | 145 | START | 145 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `12` | `11` | 148 | START | 148 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `14` | `13` | 148 | START | 148 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 148 | START | 148 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `9` | 148 | START | 148 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `11` | `10` | 148 | START | 148 | 179 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 159 | END | 145 | 159 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 168 | START | 168 | 187 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `17` | `16` | 188 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 250 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_SnapReceive` | 145 | 159 | 15 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 168 | 187 | 20 | inferred_complete_timeline |
| `Action_None` | 188 | 305 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 45 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 148 | 179 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 198 | 242 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 195 | 51 | inferred_complete_timeline |
| `Action_None` | 200 | 255 | 56 | inferred_complete_timeline |
| `Action_None` | 260 | 329 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 115 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 144 | 21 | inferred_complete_timeline |
| `Action_None` | 145 | 217 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PullBlock` | 148 | 172 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 187 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 200 | 214 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 224 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–315
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 218 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 250 | 29 | inferred_complete_timeline |
| `Action_None` | 251 | 315 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_DownBlock` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 178 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 204 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 249 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 170 | 26 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 313 | 169 | inferred_complete_timeline |
| `Action_None` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 271 | 127 | inferred_complete_timeline |
| `Action_None` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 202 | 58 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 329 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 221 | 77 | inferred_complete_timeline |
| `Action_None` | 232 | 244 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 211 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |
| `Action_None` | 145 | 187 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–188 | 149 | 7 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 29–38 | 8 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 32–123 | 89 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 136–329 | 193 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 153–158 | 6 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–322 | 162 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 173–329 | 139 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 177–185 | 9 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 193–329 | 137 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 203–329 | 127 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 218–304 | 63 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 218–246 | 29 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 223–329 | 93 | 7 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 229–326 | 96 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 234–329 | 96 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 234–329 | 96 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 237–316 | 75 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 255–290 | 31 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 273–276 | 4 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 321–329 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `17` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 730: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '11' (RG) duration 103 frames exceeds threshold 90 frames [start=148, end=250].
- ⚠️ Segment 'Action_BallCarry' for track '16' has invalid range: start=188, end=45. Clamping end to start.
- ⚠️ Action 'Action_None' range [145-249] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-255] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-202] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-271] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-313] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-221] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [148-172] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-187] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [200-214] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [220-224] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [148-179] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [187-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [198-242] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-315] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-305] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-115] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-217] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [148-158] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [179-188] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-123] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-231] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-219] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-322] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-237] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-185] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-329] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-276] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-292] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-326] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-301] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-280] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-329] for track '37' has 3 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>