# Play-Annotation-Generator Annotation Review — Counter_275

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_275`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `22` | `20` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 22 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 22 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `25` | `Group` | 0 | START | 45 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `18` | `17` | 46 | START | 46 | 52 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `18` | `17` | 53 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `19` | 53 | START | 53 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `22` | `20` | 53 | START | 53 | 56 |
| ✅ EXACT | `Action_PullBlock` | RT | `15` | `14` | 53 | START | 53 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | Position_Unknown | `18` | `17` | 53 | START | 53 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 60 | END | 46 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `13` | `12` | 64 | START | 64 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB1 | `7` | `6` | 90 | START | 90 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 61 | 63 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 78 | 89 | 12 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 104 | 59 | inferred_complete_timeline |
| `Action_None` | 108 | 137 | 30 | inferred_complete_timeline |
| `Action_None` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 134 | 89 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `25`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 45–113
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 59 | 80 | 22 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 45 | 24 | inferred_complete_timeline |
| `Action_None` | 46 | 58 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 71 | 117 | 47 | inferred_complete_timeline |
| `Action_None` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 22–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 39 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 52 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 84 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 150 | 61 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PullBlock` | 53 | 108 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 140 | 95 | inferred_complete_timeline |
| `Action_None` | 144 | 200 | 57 | inferred_complete_timeline |
| `Action_None` | 202 | 209 | 8 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 27–239
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 32 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 52 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 53 | 56 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 116 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 150 | 16 | inferred_complete_timeline |
| `Action_None` | 151 | 174 | 24 | inferred_complete_timeline |
| `Action_None` | 176 | 239 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_None` | 77 | 129 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 139 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 155 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 133 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 105 | 60 | inferred_complete_timeline |
| `Action_None` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 159 | 21 | inferred_complete_timeline |
| `Action_None` | 163 | 171 | 9 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 185 | 140 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 220 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–239 | 205 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–89 | 36 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–79 | 78 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 116–239 | 67 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 145–168 | 21 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 161–239 | 74 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 163–216 | 54 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 210–239 | 30 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 216–239 | 24 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `18` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 552: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 552: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 552: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 53 for track '17': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (RG) duration 98 frames exceeds threshold 90 frames [start=53, end=150].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (DT1) duration 98 frames exceeds threshold 90 frames [start=53, end=150].
- ⚠️ Action 'Action_None' range [46-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-139] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-173] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-133] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-200] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [64-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [72-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-105] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [53-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [53-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [62-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-117] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-34] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [53-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [53-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [58-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [62-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-104] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-225] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-216] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>