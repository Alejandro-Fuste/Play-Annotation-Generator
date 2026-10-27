# Play-Annotation-Generator Annotation Review — Counter_119

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_119`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 171
- **Validation Warnings:** 186
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
- **Inferred Coverage Segments (Action_None):** 143
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 48 | START | 48 | 63 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `17` | `16` | 51 | START | 64 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `21` | `20` | 51 | START | 51 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 51 | START | 51 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 51 | START | 51 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 51 | START | 51 | 108 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 63 | END | 48 | 63 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 78 | START | 78 | 87 |
| ✅ EXACT | `Action_BallCarry` | C | `17` | `16` | 88 | START | 88 | 108 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 115 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 64 | 77 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 88 | 113 | 26 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 73 | 26 | inferred_complete_timeline |
| `Action_None` | 77 | 119 | 43 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 169 | 122 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_None` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 107 | 60 | inferred_complete_timeline |
| `Action_None` | 109 | 269 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 51 | 108 | 58 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_None` | 116 | 152 | 37 | inferred_complete_timeline |
| `Action_None` | 155 | 269 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 78 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 92 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_None` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 136 | 143 | 8 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |
| `Action_None` | 154 | 156 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 266 | 108 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 97 | 47 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 108 | 9 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 108 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PullBlock` | 51 | 102 | 52 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 88 | 41 | inferred_complete_timeline |
| `Action_None` | 90 | 96 | 7 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 123 | 7 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_None` | 159 | 167 | 9 | inferred_complete_timeline |
| `Action_None` | 174 | 193 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 92 | 45 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 122 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 78 | 31 | inferred_complete_timeline |
| `Action_None` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 75 | 28 | inferred_complete_timeline |
| `Action_None` | 81 | 90 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 69 | 22 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 171 | 29 | inferred_complete_timeline |
| `Action_None` | 177 | 204 | 28 | inferred_complete_timeline |
| `Action_None` | 207 | 226 | 20 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 246 | 9 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 93 | 46 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 92 | 45 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_None` | 145 | 170 | 26 | inferred_complete_timeline |
| `Action_None` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 256 | 62 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 183 | 136 | inferred_complete_timeline |
| `Action_None` | 185 | 259 | 75 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 269 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 115 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 122 | 75 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 16–138 | 22 | 6 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 71–81 | 11 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 95–119 | 4 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 102–120 | 8 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 118–269 | 125 | 5 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 118–120 | 3 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 130–132 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 135–269 | 134 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 136–269 | 117 | 6 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 136–163 | 28 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 146–269 | 124 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 151–269 | 119 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 154–164 | 8 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 157–195 | 39 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 179–181 | 3 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 180–183 | 4 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 180–269 | 43 | 8 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 199–232 | 27 | 4 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 199–202 | 4 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 206–216 | 10 | 2 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 221–243 | 16 | 3 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 235–269 | 29 | 3 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 237–246 | 10 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 244–264 | 16 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `48` | `74` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `17` (C): Annotated start 51 != Inferred start 64
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 130 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_DownBlock' annotated_start=51, effective_Action_DownBlock_start=64.
- ⚠️ Action 'Action_None' range [48-169] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [51-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-226] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-246] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [51-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-92] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-108] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-266] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-193] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-78] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-90] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-122] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-113] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [51-102] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [51-97] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-108] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-24] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-203] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-163] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-158] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-195] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-207] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-252] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-264] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '48' has 1 frames without a visible bounding box.
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

</details>