# Play-Annotation-Generator Annotation Review — Counter_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_93`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 194
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 101 | START | 101 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `19` | 106 | START | 114 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 106 | START | 106 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `18` | `17` | 106 | START | 106 | 163 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `14` | `13` | 106 | START | 106 | 171 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 113 | END | 101 | 113 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 128 | START | 128 | 141 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `2` | `1` | 142 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 188 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_SnapReceive` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_None` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 141 | 14 | inferred_complete_timeline |
| `Action_None` | 142 | 271 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 209 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 198 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 106 | 171 | 66 | inferred_complete_timeline |
| `Action_None` | 194 | 370 | 177 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 366 | 266 | inferred_complete_timeline |
| `Action_None` | 374 | 376 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 137 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 167 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 188 | 9 | inferred_complete_timeline |
| `Action_None` | 189 | 289 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallSnap` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 188 | 45 | inferred_complete_timeline |
| `Action_None` | 189 | 237 | 49 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PullBlock` | 106 | 163 | 58 | inferred_complete_timeline |
| `Action_PullBlock` | 168 | 188 | 21 | inferred_complete_timeline |
| `Action_None` | 189 | 389 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |
| `Action_None` | 213 | 375 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 209 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 139 | 39 | inferred_complete_timeline |
| `Action_None` | 159 | 166 | 8 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 194 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 216 | 278 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–282
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 150 | 50 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 282 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 134 | 34 | inferred_complete_timeline |
| `Action_None` | 137 | 143 | 7 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 311 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 178 | 78 | inferred_complete_timeline |
| `Action_None` | 236 | 238 | 3 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 271 | 171 | inferred_complete_timeline |
| `Action_None` | 273 | 389 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 188 | 6 | inferred_complete_timeline |
| `Action_None` | 191 | 198 | 8 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 320 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 226 | 126 | inferred_complete_timeline |
| `Action_None` | 233 | 280 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 364 | 264 | inferred_complete_timeline |
| `Action_None` | 369 | 389 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–147 | 119 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 0–239 | 171 | 17 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 21–157 | 64 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 129–228 | 46 | 5 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 129–282 | 32 | 9 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 134–224 | 79 | 6 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 137–194 | 58 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 158–293 | 136 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 168–233 | 66 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 171–212 | 15 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 178–205 | 17 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 211–218 | 7 | 2 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 222–384 | 153 | 3 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 235–386 | 152 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 255–274 | 20 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 263–301 | 30 | 2 | Undefined position; Undefined team |
| `40` | `59` | Position_Unknown | Team_Unknown | 268–284 | 17 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 278–279 | 2 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 279–280 | 2 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 290–295 | 6 | 1 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `46` | `69` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 315–321 | 7 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 322–389 | 68 | 1 | Undefined position; Undefined team |
| `50` | `75` | Position_Unknown | Team_Unknown | 364–370 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `2` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 133 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=142, end=130. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [101–113], lower_priority='Action_DownBlock' annotated_start=106, effective_Action_DownBlock_start=114.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-278] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-282] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-366] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-311] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [106-171] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-370] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-364] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-280] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [106-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-320] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-237] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-375] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-137] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-167] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-289] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-63] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-147] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-59] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '23' starts at frame 101, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [101-108] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-161] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-202] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-34] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-221] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-228] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-282] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-154] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-201] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-233] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-366] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-386] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-274] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-282] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-284] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-321] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-370] for track '50' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.

</details>