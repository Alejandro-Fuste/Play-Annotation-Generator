# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_311`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_311/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 87 for track '13': 'Action_Handoff' vs 'Action_PressEdge'. Overriding with 'Action_PressEdge'.
> - Action 'Action_PreSnap' range [0-14] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [55-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-287] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-166] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-208] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-206] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [65-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-105] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-270] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [241-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [55-67] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-128] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-241] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-139] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-164] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-245] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-190] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-203] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-224] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '32' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.