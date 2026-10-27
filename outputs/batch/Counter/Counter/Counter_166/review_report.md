# Play-Annotation-Generator Annotation Review — Counter_166

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_166`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 93
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `15` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DE1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_BallSnap` | QB | `13` | `12` | 96 | START | 96 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | QB | `13` | `12` | 97 | START | 97 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `15` | 97 | START | 110 | 125 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | DE1 | `9` | `8` | 97 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `11` | `10` | 97 | START | 97 | 144 |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | `4` | `3` | 97 | START | 97 | 192 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `9` | `8` | 110 | END | 96 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `9` | `8` | 136 | START | 136 | 216 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 192 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_BallSnap` | 96 | 96 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 192 | 11 | inferred_complete_timeline |
| `Action_None` | 193 | 299 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 161–299
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 161 | 218 | 58 | inferred_complete_timeline |
| `Action_None` | 225 | 244 | 20 | inferred_complete_timeline |
| `Action_None` | 252 | 260 | 9 | inferred_complete_timeline |
| `Action_None` | 262 | 274 | 13 | inferred_complete_timeline |
| `Action_None` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 283 | 285 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 160 | 65 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 192 | 96 | inferred_complete_timeline |
| `Action_None` | 193 | 244 | 52 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 153 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 127 | 32 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_None` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 110–162
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 162 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 144 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 154 | 192 | 39 | inferred_complete_timeline |
| `Action_None` | 193 | 193 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 110 | 15 | inferred_complete_timeline |
| `Action_None` | 111 | 135 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 216 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 218 | 234 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 127 | 32 | inferred_complete_timeline |
| `Action_None` | 129 | 132 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 147–299
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 147 | 187 | 41 | inferred_complete_timeline |
| `Action_None` | 192 | 252 | 61 | inferred_complete_timeline |
| `Action_None` | 254 | 289 | 36 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 9–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 38 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 95 | 47 | inferred_complete_timeline |
| `Action_None` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 110 | 299 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 95 | 51 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 216 | 99 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 139 | 44 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 144 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 122 | 27 | inferred_complete_timeline |
| `Action_None` | 124 | 135 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `22` | Position_Unknown | Team_Unknown | 165–169 | 5 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 205–290 | 47 | 6 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 226–299 | 74 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 230–299 | 70 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 244–299 | 54 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 244–299 | 50 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 263–299 | 33 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | 116 | 116 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `9` (DE1)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '8' has invalid range: start=97, end=95. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '10' (C) duration 96 frames exceeds threshold 90 frames [start=97, end=192].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (QB) duration 96 frames exceeds threshold 90 frames [start=97, end=192].
- ⚠️ Action 'Action_None' range [96-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-244] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-160] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [218-234] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [97-144] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [146-151] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [154-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 193, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [193-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [97-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-162] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-289] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-218] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-244] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-274] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-279] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-282] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-285] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-277] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>