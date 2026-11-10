# Play-Annotation-Generator Annotation Review — RPO_247

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_247`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 141
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunOutRoute` | actor_track_id `17` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_PullBall` | RB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 4 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `16` | `16` | 47 | START | 47 | 52 |
| ⚠️ START CHANGED | `Action_RunBlock` | RT | `18` | `18` | 47 | START | 51 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `19` | `19` | 47 | START | 47 | 60 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | RG | `21` | `21` | 47 | START | N/A | N/A |
| ✅ EXACT | `Action_RunBlock` | LT | `8` | `8` | 47 | START | 47 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `13` | `13` | 56 | START | 56 | 123 |
| ⚠️ START CHANGED | `Action_PullBall` | RB | `20` | `20` | 74 | START | 75 | 82 |
| ✅ EXACT | `Action_ThrowPass` | RB | `20` | `20` | 98 | START | 98 | 108 |

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
- **Visible Frames:** 0–134
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 55 | 10 | inferred_complete_timeline |
| `Action_ReadDefender` | 56 | 123 | 68 | inferred_complete_timeline |
| `Action_ReadDefender` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 13 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 45 | 5 | inferred_complete_timeline |
| `Action_None` | 46 | 57 | 12 | inferred_complete_timeline |
| `Action_PullBall` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 83 | 97 | 15 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 108 | 11 | inferred_complete_timeline |
| `Action_None` | 109 | 299 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 106 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 61 | 16 | inferred_complete_timeline |
| `Action_None` | 63 | 192 | 130 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 234 | 38 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 263 | 19 | inferred_complete_timeline |
| `Action_None` | 275 | 278 | 4 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 75 | 30 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 82 | 123 | 42 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 108 | 62 | inferred_complete_timeline |
| `Action_None` | 109 | 123 | 15 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 45 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 60 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 52 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 60 | 65 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 67 | 99 | 33 | inferred_complete_timeline |
| `Action_RunBlock` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 176 | 49 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 299 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–16
- **Visible Samples:** 10

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 8 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 16 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 46 | 1 | inferred_complete_timeline |
| `Action_RunBlock` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 140 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 74 | 29 | inferred_complete_timeline |
| `Action_None` | 85 | 123 | 39 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 69 | 24 | inferred_complete_timeline |
| `Action_None` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 122 | 27 | inferred_complete_timeline |
| `Action_None` | 128 | 150 | 23 | inferred_complete_timeline |
| `Action_None` | 152 | 167 | 16 | inferred_complete_timeline |
| `Action_None` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 103 | 58 | inferred_complete_timeline |
| `Action_None` | 105 | 123 | 19 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 263 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 284 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 105 | 60 | inferred_complete_timeline |
| `Action_None` | 107 | 123 | 17 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 197 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 123 | 78 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 123 | 78 | inferred_complete_timeline |
| `Action_None` | 131 | 278 | 148 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 198 | 153 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 19–57 | 30 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 82–95 | 14 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 103–299 | 176 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 105–109 | 5 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 110–144 | 28 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 114–299 | 185 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 144–299 | 139 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 163–193 | 20 | 5 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 187–299 | 108 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 217–299 | 83 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 244–299 | 36 | 5 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (4 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `18` (RT): Annotated start 47 != Inferred start 51
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `21` (RG)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `13` (2 segments found)
- ⚠️ `Action_PullBall` for actor_track_id `20` (RB): Annotated start 74 != Inferred start 75

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 107 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_RunBlock' for track '21' has invalid range: start=47, end=16. Clamping end to start.
- ⚠️ Action 'Action_None' range [46-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-123] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-123] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-123] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-284] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-122] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [56-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [128-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-75] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-123] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [60-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [67-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [104-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 46, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [46-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [51-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-45] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [102-107] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-299] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 46, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [46-57] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [75-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-8] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-95] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-278] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-208] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-252] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-278] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '37' has 1 frames without a visible bounding box.
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