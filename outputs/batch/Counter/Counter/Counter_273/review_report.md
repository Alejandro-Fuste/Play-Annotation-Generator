# Play-Annotation-Generator Annotation Review — Counter_273

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_273`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 121 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 81 | START | 81 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 84 | START | 94 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `17` | `16` | 84 | START | 84 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `19` | `18` | 84 | START | 84 | 85 |
| ✅ EXACT | `Action_PullBlock` | LG | `14` | `13` | 84 | START | 84 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `3` | `2` | 84 | START | 84 | 138 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 93 | END | 81 | 93 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 107 | START | 107 | 121 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 122 | START | 122 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 94 | 106 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 107 | 121 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 389 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_BallCarry` | 122 | 389 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 389 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 281 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 80 | 61 | inferred_complete_timeline |
| `Action_None` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_None` | 169 | 232 | 64 | inferred_complete_timeline |
| `Action_None` | 234 | 389 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 84 | 138 | 55 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 144 | 64 | inferred_complete_timeline |
| `Action_None` | 146 | 156 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PullBlock` | 84 | 146 | 63 | inferred_complete_timeline |
| `Action_None` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_None` | 158 | 163 | 6 | inferred_complete_timeline |
| `Action_None` | 165 | 389 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 102 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 146 | 15 | inferred_complete_timeline |
| `Action_None` | 147 | 240 | 94 | inferred_complete_timeline |
| `Action_None` | 287 | 309 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 83 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 100 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 146 | 31 | inferred_complete_timeline |
| `Action_None` | 147 | 188 | 42 | inferred_complete_timeline |
| `Action_None` | 191 | 240 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 83 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 106 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 139 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 141 | 145 | 5 | inferred_complete_timeline |
| `Action_None` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 183 | 389 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 167 | 87 | inferred_complete_timeline |
| `Action_None` | 170 | 389 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 125 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 80 | 61 | inferred_complete_timeline |
| `Action_None` | 81 | 111 | 31 | inferred_complete_timeline |
| `Action_None` | 161 | 240 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 389 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 134 | 54 | inferred_complete_timeline |
| `Action_None` | 147 | 156 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 330 | 250 | inferred_complete_timeline |
| `Action_None` | 333 | 340 | 8 | inferred_complete_timeline |
| `Action_None` | 343 | 346 | 4 | inferred_complete_timeline |
| `Action_None` | 348 | 389 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 136 | 56 | inferred_complete_timeline |
| `Action_None` | 140 | 389 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 127 | 47 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |
| `Action_None` | 241 | 248 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 379 | 299 | inferred_complete_timeline |
| `Action_None` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 389 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 272 | 192 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 281 | 286 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 18–20 | 3 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 157–165 | 9 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–389 | 227 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 170–234 | 49 | 5 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 173–389 | 209 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 175–389 | 215 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 176–389 | 173 | 6 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 272–389 | 118 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 282–389 | 108 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 290–389 | 100 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 295–304 | 10 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 296–389 | 94 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 321–337 | 17 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 326–332 | 7 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 366–389 | 24 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 370–389 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [81–93], lower_priority='Action_DownBlock' annotated_start=84, effective_Action_DownBlock_start=94.
- ⚠️ Action 'Action_None' range [81-379] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [84-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [140-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [145-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-330] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-340] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-145] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-389] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-240] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-93] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-232] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-165] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-178] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-389] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-213] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-378] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-389] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-337] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-332] for track '35' has 1 frames without a visible bounding box.
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

</details>