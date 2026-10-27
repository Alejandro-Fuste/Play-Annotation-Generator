# Play-Annotation-Generator Annotation Review — Counter_201

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_201`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 53
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_DownBlock` | LB2 | defense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `21` | `20` | 91 | START | 91 | 101 |
| ✅ EXACT | `Action_DownBlock` | LT | `2` | `1` | 93 | START | 93 | 119 |
| ✅ EXACT | `Action_DownBlock` | LB2 | `8` | `7` | 93 | START | 93 | 163 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | LG | `9` | `8` | 93 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 93 | START | 93 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LG | `9` | `8` | 93 | START | 93 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 105 | END | 91 | 105 |
| ✅ EXACT | `Action_BallCarry` | QB | `20` | `19` | 134 | START | 134 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 105 | 15 | inferred_complete_timeline |
| `Action_None` | 106 | 120 | 15 | inferred_complete_timeline |
| `Action_None` | 122 | 133 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 149 | 59 | inferred_complete_timeline |
| `Action_None` | 154 | 239 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 119 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 93 | 113 | 21 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 129 | 163 | 35 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 91 | 101 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 118 | 13 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 127 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 146 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_None` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 127 | 37 | inferred_complete_timeline |
| `Action_None` | 130 | 139 | 10 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 126 | 36 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 127 | 37 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 127 | 37 | inferred_complete_timeline |
| `Action_None` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 112 | 22 | inferred_complete_timeline |
| `Action_None` | 116 | 127 | 12 | inferred_complete_timeline |
| `Action_None` | 130 | 149 | 20 | inferred_complete_timeline |
| `Action_None` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 222 | 132 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 163 | 71 | inferred_complete_timeline |
| `Action_None` | 164 | 220 | 57 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 218 | 128 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_None` | 91 | 239 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 123–154 | 8 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 134–138 | 5 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 137–239 | 103 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 153–239 | 87 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 189–193 | 5 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `9` (LG)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 35 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 93 for track '8': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Action 'Action_None' range [91-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-119] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-127] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-127] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [93-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [115-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [126-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-127] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [91-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [103-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-138] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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