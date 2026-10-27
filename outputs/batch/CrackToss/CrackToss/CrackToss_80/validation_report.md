# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_80`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [59-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-139] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-137] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-83] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-144] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-117] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-120] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [67-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-35] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-50] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [62-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [88-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-103] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-103] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-127] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-135] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '32' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.