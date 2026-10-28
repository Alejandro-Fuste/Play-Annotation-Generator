# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_9`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [44–59], lower_priority='Action_PassBlock' annotated_start=47, effective_Action_PassBlock_start=60.
> - Action 'Action_None' range [44-106] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-149] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-200] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [121-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-76] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [44-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-151] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-193] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.