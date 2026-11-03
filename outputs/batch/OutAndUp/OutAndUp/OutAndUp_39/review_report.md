# Play-Annotation-Generator Annotation Review — OutAndUp_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_39`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 55
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 167
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
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 113
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SellOut` | WR3 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 12 | START | 12 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 15 | START | 15 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 15 | START | 29 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `18` | 15 | START | 15 | 93 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 15 | START | 15 | 82 |
| ✅ EXACT | `Action_PassBlock` | LT | `4` | `4` | 15 | START | 15 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 28 | END | 12 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_SellOut` | WR3 | `1` | `1` | 78 | START | 79 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunGoRoute` | WR3 | `1` | `1` | 94 | START | 94 | 120 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 106 | START | 106 | 117 |

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
- **Visible Frames:** 0–175
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 105 | 77 | inferred_complete_timeline |
| `Action_ThrowPass` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 127 | 10 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 117 | 106 | inferred_complete_timeline |
| `Action_None` | 123 | 153 | 31 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 172 | 186 | 15 | inferred_complete_timeline |
| `Action_None` | 190 | 216 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 137 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 176 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 125 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SellOut` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_SellOut` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_RunGoRoute` | 94 | 120 | 27 | inferred_complete_timeline |
| `Action_RunGoRoute` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 127 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 82 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 56 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 127 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 93 | 79 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 98 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 55 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 84 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 86 | 128 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 127 | 116 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 58 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 130 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 102 | 91 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 221 | 210 | inferred_complete_timeline |
| `Action_None` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 221 | 210 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 92 | 81 | inferred_complete_timeline |
| `Action_None` | 95 | 226 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 175 | 87 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 179 | 168 | inferred_complete_timeline |
| `Action_None` | 181 | 203 | 23 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 224 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 184 | 173 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 99–175 | 65 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 113–123 | 11 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 123–239 | 114 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 137–239 | 103 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 138–155 | 18 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 152–175 | 24 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 158–203 | 42 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 158–239 | 44 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 164–239 | 76 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 167–239 | 31 | 5 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 169–181 | 13 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 169–239 | 71 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 176–181 | 6 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 184–239 | 53 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 184–187 | 4 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 185–239 | 55 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 185–209 | 22 | 3 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 193–203 | 4 | 2 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 194–239 | 46 | 1 | Undefined position; Undefined team |
| `43` | `49` | Position_Unknown | Team_Unknown | 195–239 | 44 | 2 | Undefined position; Undefined team |
| `44` | `50` | Position_Unknown | Team_Unknown | 197–239 | 43 | 1 | Undefined position; Undefined team |
| `45` | `51` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |
| `46` | `52` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `47` | `53` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `48` | `55` | Position_Unknown | Team_Unknown | 203–227 | 22 | 2 | Undefined position; Undefined team |
| `49` | `57` | Position_Unknown | Team_Unknown | 203–222 | 20 | 1 | Undefined position; Undefined team |
| `50` | `59` | Position_Unknown | Team_Unknown | 213–232 | 19 | 2 | Undefined position; Undefined team |
| `51` | `60` | Position_Unknown | Team_Unknown | 214–226 | 4 | 2 | Undefined position; Undefined team |
| `52` | `61` | Position_Unknown | Team_Unknown | 214–232 | 15 | 2 | Undefined position; Undefined team |
| `53` | `63` | Position_Unknown | Team_Unknown | 229–232 | 4 | 1 | Undefined position; Undefined team |
| `54` | `64` | Position_Unknown | Team_Unknown | 233–239 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SellOut` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunGoRoute` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [12–28], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [12-176] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [79-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [94-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [122-125] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-58] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-127] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-184] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-179] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-203] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-55] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-84] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [86-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-127] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-186] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-216] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-221] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-161] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-181] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-239] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-196] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-239] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-218] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-222] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-232] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '53' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.

</details>