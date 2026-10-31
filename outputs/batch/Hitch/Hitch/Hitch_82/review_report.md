# Play-Annotation-Generator Annotation Review — Hitch_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_82`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 145
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 125
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunHitchRoute` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 4 | START | 4 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `14` | 7 | START | 7 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 7 | START | 7 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 7 | START | 21 | 63 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `2` | 7 | START | 7 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 7 | START | 7 | 124 |
| ✅ EXACT | `Action_RunHitchRoute` | WR3 | `3` | `3` | 20 | START | 20 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 20 | END | 4 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | QB | `20` | `20` | 104 | START | 104 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `3` | `3` | 153 | START | 153 | 355 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_None` | 21 | 103 | 83 | inferred_complete_timeline |
| `Action_ThrowPass` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_ThrowPass` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 116 | 113 | inferred_complete_timeline |
| `Action_None` | 120 | 122 | 3 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 146 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 198 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 173 | 170 | inferred_complete_timeline |
| `Action_None` | 176 | 419 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–370
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 20 | 118 | 99 | inferred_complete_timeline |
| `Action_None` | 119 | 152 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 355 | 203 | inferred_complete_timeline |
| `Action_BallCarry` | 360 | 370 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 67 | 64 | inferred_complete_timeline |
| `Action_None` | 74 | 111 | 38 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 152 | 158 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 263 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 124 | 118 | inferred_complete_timeline |
| `Action_PassBlock` | 129 | 419 | 291 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 77 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 116 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 149 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 231 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 51 | 45 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 108 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 147 | 141 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 235 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 106 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 46 | 43 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 63 | 114 | 52 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 96 | 93 | inferred_complete_timeline |
| `Action_None` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 194 | 419 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 53 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 74 | 71 | inferred_complete_timeline |
| `Action_None` | 76 | 115 | 40 | inferred_complete_timeline |
| `Action_None` | 118 | 137 | 20 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 419 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 84 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–413
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 143 | 140 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 348 | 179 | inferred_complete_timeline |
| `Action_None` | 350 | 413 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 132 | 129 | inferred_complete_timeline |
| `Action_None` | 134 | 242 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 204 | 201 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 399 | 188 | inferred_complete_timeline |
| `Action_None` | 407 | 419 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 129 | 126 | inferred_complete_timeline |
| `Action_None` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_None` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_None` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_None` | 185 | 391 | 207 | inferred_complete_timeline |
| `Action_None` | 393 | 419 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 8 | 5 | inferred_complete_timeline |
| `Action_None` | 12 | 158 | 147 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_None` | 173 | 189 | 17 | inferred_complete_timeline |
| `Action_None` | 191 | 273 | 83 | inferred_complete_timeline |
| `Action_None` | 277 | 360 | 84 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 376 | 5 | inferred_complete_timeline |
| `Action_None` | 378 | 401 | 24 | inferred_complete_timeline |
| `Action_None` | 403 | 406 | 4 | inferred_complete_timeline |
| `Action_None` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 60–116 | 55 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–70 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 135–419 | 243 | 8 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 137–235 | 62 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 141–384 | 234 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 169–237 | 69 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 169–419 | 248 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 194–419 | 226 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 197–419 | 223 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 199–419 | 220 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 254–419 | 166 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 255–419 | 165 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 257–419 | 163 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 260–395 | 135 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 330–419 | 90 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 339–341 | 3 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 377–419 | 43 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 399–402 | 4 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 408–419 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 105 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [4–20], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=21.
- ⚠️ Action 'Action_None' range [4-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-263] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-355] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [360-370] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-67] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-111] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-348] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-413] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-132] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-204] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-399] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-147] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-158] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-360] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-401] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-391] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-108] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [104-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [129-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-83] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-209] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-384] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-346] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-416] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-282] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-395] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-419] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-419] for track '40' has 1 frames without a visible bounding box.
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