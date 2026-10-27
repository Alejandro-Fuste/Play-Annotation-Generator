# Play-Annotation-Generator Annotation Review — Counter_369

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_369`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `23` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 36 | START | 36 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `19` | `18` | 39 | START | 39 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 39 | START | 39 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `21` | `20` | 39 | START | 52 | 55 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `5` | `4` | 39 | START | 39 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 50 | END | 36 | 50 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 62 | START | 62 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 73 | START | 73 | 78 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–225
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 50 | 15 | inferred_complete_timeline |
| `Action_None` | 51 | 61 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_None` | 73 | 130 | 58 | inferred_complete_timeline |
| `Action_None` | 132 | 165 | 34 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 179 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 213 | 15 | inferred_complete_timeline |
| `Action_None` | 218 | 225 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 72 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 99 | 108 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 135 | 100 | inferred_complete_timeline |
| `Action_None` | 137 | 239 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 190 | 155 | inferred_complete_timeline |
| `Action_None` | 192 | 195 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 39 | 73 | 35 | inferred_complete_timeline |
| `Action_None` | 110 | 168 | 59 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 59 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 45 | 10 | inferred_complete_timeline |
| `Action_None` | 48 | 73 | 26 | inferred_complete_timeline |
| `Action_None` | 78 | 128 | 51 | inferred_complete_timeline |
| `Action_None` | 132 | 168 | 37 | inferred_complete_timeline |
| `Action_None` | 171 | 191 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_BallSnap` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 57 | 62 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 69 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 39 | 70 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 81 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 101 | 66 | inferred_complete_timeline |
| `Action_None` | 109 | 126 | 18 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 186 | 55 | inferred_complete_timeline |
| `Action_None` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 149 | 114 | inferred_complete_timeline |
| `Action_None` | 152 | 226 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 54 | 19 | inferred_complete_timeline |
| `Action_None` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_None` | 72 | 107 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 91 | 56 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 202 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 129 | 94 | inferred_complete_timeline |
| `Action_None` | 131 | 174 | 44 | inferred_complete_timeline |
| `Action_None` | 177 | 184 | 8 | inferred_complete_timeline |
| `Action_None` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 82 | 47 | inferred_complete_timeline |
| `Action_None` | 87 | 118 | 32 | inferred_complete_timeline |
| `Action_None` | 122 | 159 | 38 | inferred_complete_timeline |
| `Action_None` | 162 | 202 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 239 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 199 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–239 | 198 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–41 | 13 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 58–59 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 62–173 | 100 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 79–147 | 54 | 6 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 86–121 | 31 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 90–179 | 90 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 100–180 | 77 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 111–237 | 118 | 5 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 121–190 | 63 | 3 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 133–221 | 75 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 136–176 | 37 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 179–189 | 9 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 740: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [36–50], lower_priority='Action_PullBlock' annotated_start=39, effective_Action_PullBlock_start=51.
- ⚠️ Action 'Action_None' range [36-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-135] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-239] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-190] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-126] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-186] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [39-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-69] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-107] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-82] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-118] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [99-108] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-202] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-239] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-149] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-226] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-91] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [39-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [36-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [52-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [57-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [39-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [59-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-191] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-153] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-91] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-110] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-179] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-209] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-173] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-221] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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