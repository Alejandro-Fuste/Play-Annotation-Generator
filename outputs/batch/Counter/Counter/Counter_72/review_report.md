# Play-Annotation-Generator Annotation Review — Counter_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_72`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LB1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `18` | `17` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 4 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 10 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 62 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `23` | `Group` | 0 | START | 73 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 85 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `14` | `13` | 139 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `14` | `13` | 144 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `5` | `4` | 144 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LB1 | `11` | `10` | 144 | START | 144 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `18` | `17` | 144 | START | 144 | 145 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `3` | `2` | 147 | START | 147 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 152 | END | 139 | 152 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 165 | START | 165 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 175 | START | 175 | 181 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 201 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–179
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_SnapReceive` | 139 | 152 | 14 | inferred_complete_timeline |
| `Action_None` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 165 | 173 | 9 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 146 | 147 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 147 | 174 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 243 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 10–153
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 14 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 24 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 143 | 111 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 138 | 40 | inferred_complete_timeline |
| `Action_None` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 201 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `23`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 73–155
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 73 | 138 | 66 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 148 | 155 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 62–150
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 138 | 77 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 4–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 39 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 138 | 84 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 138 | 44 | inferred_complete_timeline |
| `Action_None` | 139 | 209 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 183 | 45 | inferred_complete_timeline |
| `Action_None` | 187 | 189 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 138 | 111 | inferred_complete_timeline |
| `Action_None` | 139 | 170 | 32 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 51–223
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 51 | 138 | 88 | inferred_complete_timeline |
| `Action_None` | 139 | 156 | 18 | inferred_complete_timeline |
| `Action_None` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 197 | 54 | inferred_complete_timeline |
| `Action_PullBlock` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 214 | 13 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 199 | 61 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 138 | 74 | inferred_complete_timeline |
| `Action_None` | 139 | 276 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 222 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 222 | 84 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–16 | 17 | 1 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–49 | 50 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–19 | 20 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–299 | 271 | 7 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–64 | 57 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 74–223 | 68 | 7 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 158–170 | 13 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 161–299 | 113 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 168–272 | 69 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 192–196 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 198–299 | 100 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 209–299 | 87 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 209–213 | 5 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 224–226 | 3 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 224–299 | 68 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 266–268 | 3 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `14` (Position_Unknown)
- ❌ Missing segment for action `Action_DownBlock` on target `14` (Position_Unknown)
- ❌ Missing segment for action `Action_DownBlock` on target `5` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 146: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '4' has invalid range: start=144, end=16. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '13' has invalid range: start=139, end=64. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '13' has invalid range: start=144, end=64. Clamping end to start.
- ⚠️ Action 'Action_None' range [139-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [147-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [199-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [236-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-201] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-209] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [165-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [144-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-214] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-222] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-276] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-24] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [152-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-114] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-202] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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