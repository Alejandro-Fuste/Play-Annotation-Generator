# Play-Annotation-Generator Annotation Review — Slants0to10_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 99
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
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunSlantRoute` | WR4 | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | RG | `20` | `20` | 1 | START | 1 | 3 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 4 | START | 4 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 4 | START | 4 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 4 | START | 4 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `5` | `5` | 4 | START | 4 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 4 | START | 4 | 42 |
| ✅ EXACT | `Action_RunSlantRoute` | WR4 | `16` | `16` | 11 | START | 11 | 77 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 11 | END | 1 | 11 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 68 | START | 68 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR4 | `16` | `16` | 117 | START | 117 | 193 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 11 | 11 | inferred_complete_timeline |
| `Action_None` | 12 | 67 | 56 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 77 | 10 | inferred_complete_timeline |
| `Action_None` | 78 | 180 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 119 | 119 | inferred_complete_timeline |
| `Action_None` | 124 | 226 | 103 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 198 | 198 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 221 | 13 | inferred_complete_timeline |
| `Action_None` | 223 | 239 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 72 | 72 | inferred_complete_timeline |
| `Action_None` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 11 | 77 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 116 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 193 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 100 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 168 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 178 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 85 | 82 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 23 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 28 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 3 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 10 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 14 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 35 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 60 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 42 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 239 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 77 | 77 | inferred_complete_timeline |
| `Action_None` | 80 | 111 | 32 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 43 | 43 | inferred_complete_timeline |
| `Action_None` | 45 | 54 | 10 | inferred_complete_timeline |
| `Action_None` | 59 | 223 | 165 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 185 | 185 | inferred_complete_timeline |
| `Action_None` | 189 | 193 | 5 | inferred_complete_timeline |
| `Action_None` | 202 | 239 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 98 | 98 | inferred_complete_timeline |
| `Action_None` | 106 | 239 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 131 | 131 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 239 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 59 | 59 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 184 | 184 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 213 | 213 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 21–22 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 30–239 | 197 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 58–59 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 61–64 | 4 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 70–84 | 5 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 85–102 | 18 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 87–89 | 3 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 128–239 | 112 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 195–206 | 8 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 197–210 | 12 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 213–239 | 27 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 227–239 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 63 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [1-72] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-100] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-168] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-42] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-43] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-223] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-193] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-185] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-77] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-85] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-35] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-23] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-22] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-31] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-51] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-214] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-102] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>