# Play-Annotation-Generator Annotation Review — Counter_301

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_301`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | defense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 39 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `7` | `6` | 30 | END | 40 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 40 | START | 40 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF2 | `17` | `16` | 43 | START | 43 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `19` | `18` | 43 | START | 43 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 43 | START | 43 | 43 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `17` | 43 | START | 43 | 126 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `20` | `19` | 43 | START | 43 | 126 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 61 | START | 61 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 80 | START | 80 | 113 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 126 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 61 | 79 | 19 | inferred_complete_timeline |
| `Action_None` | 80 | 173 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 113 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 123 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 209 | 170 | inferred_complete_timeline |
| `Action_None` | 211 | 246 | 36 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 168 | 129 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 256 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 205 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 59 | 20 | inferred_complete_timeline |
| `Action_None` | 68 | 291 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 47 | 79 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 54 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 126 | 26 | inferred_complete_timeline |
| `Action_None` | 127 | 190 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PullBlock` | 43 | 126 | 84 | inferred_complete_timeline |
| `Action_None` | 127 | 147 | 21 | inferred_complete_timeline |
| `Action_None` | 149 | 205 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 43 | 126 | 84 | inferred_complete_timeline |
| `Action_None` | 127 | 148 | 22 | inferred_complete_timeline |
| `Action_None` | 162 | 196 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 93 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 176 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 84 | 45 | inferred_complete_timeline |
| `Action_None` | 87 | 202 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_None` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_None` | 81 | 85 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 264 | 173 | inferred_complete_timeline |
| `Action_None` | 266 | 276 | 11 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |
| `Action_None` | 286 | 289 | 4 | inferred_complete_timeline |
| `Action_None` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 188 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 278 | 239 | inferred_complete_timeline |
| `Action_None` | 284 | 299 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 233 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 201 | 162 | inferred_complete_timeline |
| `Action_None` | 204 | 250 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 185 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 299 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 89 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 92 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 87–299 | 211 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 96–115 | 20 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 105–211 | 100 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 118–262 | 143 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 145–198 | 54 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 182–184 | 3 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 212–216 | 5 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 228–299 | 63 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 246–299 | 36 | 5 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 279–299 | 21 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 281–299 | 19 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 285–299 | 15 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 288–299 | 12 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 291–299 | 9 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '6' has invalid range: start=40, end=30. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=40, end=30. Clamping end to start.
- ⚠️ Action 'Action_None' range [40-209] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-246] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-56] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-264] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-276] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-201] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-250] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-113] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-278] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-291] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-188] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-176] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [91-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [43-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-205] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-54] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [43-126] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '20' starts at frame 43, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [43-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [47-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-295] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-211] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-283] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '36' has 1 frames without a visible bounding box.
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