# Play-Annotation-Generator Annotation Review — Counter_379

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_379`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `17` |
| ⚠️ START CHANGED | `Action_DownBlock` | LT | offense | `23` | `20` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 7 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `23` | `Group` | 0 | START | 12 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 49 | START | 49 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `17` | 52 | START | 52 | 53 |
| ⚠️ START CHANGED | `Action_DownBlock` | LT | `23` | `20` | 52 | START | 82 | 89 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | QB | `14` | `13` | 52 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `13` | `12` | 52 | START | 52 | 60 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 61 | END | 49 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `14` | `13` | 76 | START | 76 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 92 | START | 92 | 95 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 61 | 13 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 66 | 75 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 194 | 199 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 127 | 79 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `23`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 12–89
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 16 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 82 | 89 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 7–210
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 51 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 58 | 10 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 53 | 5 | inferred_complete_timeline |
| `Action_None` | 78 | 89 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 60 | 9 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 78 | 89 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 16 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 37 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_None` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 177 | 69 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 10–210
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 16 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 45 | 3 | inferred_complete_timeline |
| `Action_None` | 77 | 103 | 27 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 162 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 210 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 53 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 59 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 2–49
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 17 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 48 | 26 | inferred_complete_timeline |
| `Action_None` | 49 | 49 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 75 | 90 | 16 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 210 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 118 | 70 | inferred_complete_timeline |
| `Action_None` | 121 | 143 | 23 | inferred_complete_timeline |
| `Action_None` | 147 | 210 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 172 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 128 | 80 | inferred_complete_timeline |
| `Action_None` | 133 | 158 | 26 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `24` | Position_Unknown | Team_Unknown | 69–210 | 118 | 6 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 83–90 | 8 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 83–210 | 75 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 112–210 | 91 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 117–120 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 155–210 | 56 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 155–178 | 10 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 157–210 | 53 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 157–210 | 52 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 158–210 | 36 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 174–210 | 37 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 183–210 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `23` (LT): Annotated start 52 != Inferred start 82
- ❌ Missing segment for action `Action_PullBlock` on target `14` (QB)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_PullBlock' for track '13' has invalid range: start=52, end=48. Clamping end to start.
- ⚠️ Action 'Action_None' range [49-127] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-118] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-158] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [52-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [78-89] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [76-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [49-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 49, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [49-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-118] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-37] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-48] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-89] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [82-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-79] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-136] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-210] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>