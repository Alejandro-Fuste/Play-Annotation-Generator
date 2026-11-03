# Play-Annotation-Generator Annotation Review — Post10to15_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_35`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 152
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 20 | START | 20 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `12` | `12` | 23 | START | 36 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 23 | START | 23 | 49 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 23 | START | 23 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 23 | START | 23 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 23 | START | 23 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR1 | `1` | `1` | 35 | START | 35 | 58 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 35 | END | 20 | 35 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 80 | START | 80 | 87 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_None` | 36 | 79 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 80 | 87 | 8 | inferred_complete_timeline |
| `Action_None` | 88 | 210 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 46 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunPostRoute` | 35 | 58 | 24 | inferred_complete_timeline |
| `Action_RunPostRoute` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_RunPostRoute` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_RunPostRoute` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_RunPostRoute` | 80 | 116 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 171 | 152 | inferred_complete_timeline |
| `Action_None` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 80 | 61 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 151 | 19 | inferred_complete_timeline |
| `Action_None` | 153 | 175 | 23 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 49 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 80 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 105 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 42 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_BallSnap` | 20 | 35 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 70 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 116 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 47 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 130 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 136 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 210 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_None` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_None` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_None` | 51 | 84 | 34 | inferred_complete_timeline |
| `Action_None` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 210 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_None` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 80 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 83 | 64 | inferred_complete_timeline |
| `Action_None` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_None` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 104 | 121 | 18 | inferred_complete_timeline |
| `Action_None` | 141 | 159 | 19 | inferred_complete_timeline |
| `Action_None` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 48 | 29 | inferred_complete_timeline |
| `Action_None` | 51 | 64 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 147 | 128 | inferred_complete_timeline |
| `Action_None` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 169 | 150 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 171 | 152 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 186 | 196 | 11 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 88 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_None` | 20 | 175 | 156 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 56–210 | 88 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 57–119 | 45 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 62–125 | 52 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 98–210 | 109 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 108–210 | 62 | 6 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 123–210 | 88 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 143–157 | 15 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 145–175 | 31 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 146–210 | 65 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 147–210 | 62 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 147–204 | 57 | 2 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 172–210 | 39 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 176–210 | 33 | 3 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 181–210 | 30 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `1` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 117 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [20–35], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=36.
- ⚠️ Action 'Action_None' range [20-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-121] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [35-58] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [60-62] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [65-68] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [70-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [80-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-80] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-42] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-169] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-64] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-48] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-49] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-42] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-42] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-47] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [146-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-126] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-159] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-157] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-204] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-196] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '37' has 1 frames without a visible bounding box.
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