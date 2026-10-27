# Play-Annotation-Generator Annotation Review — Counter_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_71`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 125
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
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 99 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 100 | START | 100 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `3` | `2` | 108 | START | 108 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 109 | START | 113 | 117 |
| ✅ EXACT | `Action_DownBlock` | RT | `21` | `20` | 109 | START | 109 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `22` | `21` | 109 | START | 109 | 128 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 110 | START | 110 | 137 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 112 | END | 100 | 112 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 125 | START | 125 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 138 | START | 138 | 150 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_SnapReceive` | 100 | 112 | 13 | inferred_complete_timeline |
| `Action_None` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 110 | 137 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 135 | 36 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 299 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 258 | 159 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 132 | 25 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 240 | 15 | inferred_complete_timeline |
| `Action_None` | 242 | 286 | 45 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 124 | 25 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 179 | 12 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 263 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 125 | 26 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_PullBlock` | 109 | 128 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 139 | 143 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_BallSnap` | 100 | 112 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 117 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 120 | 21 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 128 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 132 | 33 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 119 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 129 | 8 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 145 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 119 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 272 | 78 | inferred_complete_timeline |
| `Action_None` | 279 | 285 | 7 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 119 | 20 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 128 | 29 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 132 | 33 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 136 | 163 | 28 | inferred_complete_timeline |
| `Action_None` | 166 | 232 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 299 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 299 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 161 | 62 | inferred_complete_timeline |
| `Action_None` | 173 | 178 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_None` | 100 | 262 | 163 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_None` | 275 | 294 | 20 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 10–14 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 159–299 | 140 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 173–241 | 53 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 186–299 | 111 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 192–299 | 92 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 193–299 | 105 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 193–299 | 107 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 200–299 | 75 | 8 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 212–299 | 88 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 212–299 | 87 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 230–232 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 241–243 | 3 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 260–299 | 35 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [100–112], lower_priority='Action_DownBlock' annotated_start=109, effective_Action_DownBlock_start=113.
- ⚠️ Action 'Action_None' range [100-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-135] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [141-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [168-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-240] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-286] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-262] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-294] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-125] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [127-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-272] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-133] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-163] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-232] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [109-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [139-143] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-294] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-230] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-299] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-268] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-290] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-299] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-228] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-259] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-299] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-277] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-243] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-285] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '38' has 1 frames without a visible bounding box.
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