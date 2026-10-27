# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_164`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_164/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 329: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [71-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [73-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-115] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [73-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [73-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-104] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [115-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-129] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [78-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-165] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-154] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-179] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '28' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.