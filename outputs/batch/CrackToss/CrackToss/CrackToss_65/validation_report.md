# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_65`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 132: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 132: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [58-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-104] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-149] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [61-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [99-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-161] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-141] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-75] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-154] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-175] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-129] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-123] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [131-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-100] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-153] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-127] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-175] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-154] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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