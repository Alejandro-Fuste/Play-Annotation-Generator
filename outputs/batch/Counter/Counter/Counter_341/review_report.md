# Play-Annotation-Generator Annotation Review — Counter_341

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_341`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 118
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
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `15` | `14` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 101 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 102 | START | 102 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `15` | `14` | 105 | START | 105 | 141 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `16` | `15` | 105 | START | 115 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE1 | `20` | `19` | 105 | START | 105 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `17` | `16` | 105 | START | 105 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `4` | `3` | 105 | START | 105 | 178 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 114 | END | 102 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 131 | START | 131 | 143 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 144 | START | 144 | 207 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 191 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_SnapReceive` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 115 | 130 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 131 | 143 | 13 | inferred_complete_timeline |
| `Action_None` | 144 | 299 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 207 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 140 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 191 | 49 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 197 | 208 | 12 | inferred_complete_timeline |
| `Action_None` | 210 | 233 | 24 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 249 | 299 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 105 | 178 | 74 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 180 | 191 | 12 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 267 | 71 | inferred_complete_timeline |
| `Action_None` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 149 | 45 | inferred_complete_timeline |
| `Action_PullBlock` | 155 | 159 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 191 | 77 | inferred_complete_timeline |
| `Action_None` | 192 | 283 | 92 | inferred_complete_timeline |
| `Action_None` | 288 | 292 | 5 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 141 | 37 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 191 | 20 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 214 | 9 | inferred_complete_timeline |
| `Action_None` | 222 | 299 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 155 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 214 | 113 | inferred_complete_timeline |
| `Action_None` | 219 | 290 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 194 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 126 | 25 | inferred_complete_timeline |
| `Action_None` | 128 | 181 | 54 | inferred_complete_timeline |
| `Action_None` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_None` | 192 | 202 | 11 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 237 | 299 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 165 | 64 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 180 | 209 | 30 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 233 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 197 | 96 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 171 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 155 | 54 | inferred_complete_timeline |
| `Action_None` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 213 | 112 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_None` | 102 | 222 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 147–262 | 110 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 147–299 | 145 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 150–181 | 4 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 173–182 | 6 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 182–229 | 30 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 198–299 | 99 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 199–236 | 13 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 201–299 | 99 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 204–299 | 88 | 4 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 206–299 | 94 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 235–299 | 17 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 249–299 | 33 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 283–286 | 4 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (4 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `16` (C): Annotated start 105 != Inferred start 115
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [102–114], lower_priority='Action_DownBlock' annotated_start=105, effective_Action_DownBlock_start=115.
- ⚠️ Action 'Action_None' range [102-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-290] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [105-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [180-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-267] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-155] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-194] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-160] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [155-159] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-197] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-209] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-229] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-299] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '39' has 1 frames without a visible bounding box.
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

</details>