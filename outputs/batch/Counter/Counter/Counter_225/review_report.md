# Play-Annotation-Generator Annotation Review — Counter_225

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_225`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB2 | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 8 | START | 8 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `11` | `Group` | 8 | START | 8 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 8 | START | 8 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 8 | START | 8 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 8 | START | 8 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 8 | START | 8 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 8 | START | 8 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 8 | START | 8 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 8 | START | 8 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 8 | START | 8 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 8 | START | 8 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 72 | START | 72 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 74 | START | 88 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `19` | `18` | 74 | START | 74 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `3` | 74 | START | 74 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 74 | START | 74 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `7` | `6` | 74 | START | 74 | 152 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB2 | `11` | `10` | 77 | START | 77 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 87 | END | 72 | 87 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 103 | START | 103 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | `11` | `10` | 126 | START | 126 | 272 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 165 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 72 | 87 | 16 | inferred_complete_timeline |
| `Action_None` | 88 | 102 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 103 | 125 | 23 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 8–139
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 139 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 8–305
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 76 | 69 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 77 | 125 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 272 | 147 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 302 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 304 | 305 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 8–300
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 300 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 329 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 73 | 66 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 74 | 152 | 79 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 73 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 165 | 41 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 73 | 66 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 91 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 145 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 8–110
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 72 | 87 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 73 | 66 | inferred_complete_timeline |
| `Action_PullBlock` | 74 | 127 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 137 | 165 | 29 | inferred_complete_timeline |
| `Action_None` | 166 | 329 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 112 | 41 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_None` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–152
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 114 | 43 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 152 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 329 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 8–150
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 112 | 41 | inferred_complete_timeline |
| `Action_None` | 121 | 256 | 136 | inferred_complete_timeline |
| `Action_None` | 258 | 329 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 141 | 70 | inferred_complete_timeline |
| `Action_None` | 145 | 329 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 156 | 85 | inferred_complete_timeline |
| `Action_None` | 172 | 329 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 317 | 246 | inferred_complete_timeline |
| `Action_None` | 319 | 329 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 329 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 185 | 114 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 204 | 10 | inferred_complete_timeline |
| `Action_None` | 212 | 329 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 315 | 244 | inferred_complete_timeline |
| `Action_None` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 329 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 72 | 329 | 258 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 105–329 | 220 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 110–329 | 186 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 138–144 | 4 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 155–329 | 167 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 159–167 | 5 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 159–329 | 171 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 249–322 | 46 | 5 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 268–299 | 31 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 268–284 | 16 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 270–297 | 16 | 3 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 270–306 | 26 | 2 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 288–311 | 7 | 2 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 318–326 | 9 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 92 frames exceeds threshold 90 frames [start=74, end=165].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [72–87], lower_priority='Action_DownBlock' annotated_start=74, effective_Action_DownBlock_start=88.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 92 frames exceeds threshold 90 frames [start=74, end=165].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 92 frames exceeds threshold 90 frames [start=74, end=165].
- ⚠️ Action 'Action_None' range [72-317] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-300] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-104] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [74-152] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-185] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-272] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-302] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [304-305] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-329] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-256] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [101-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-112] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-93] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [74-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [96-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [104-145] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-159] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-141] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [74-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [137-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-188] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-329] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-277] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-294] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-306] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '35' has 1 frames without a visible bounding box.
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