# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_204`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_204/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-189] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-155] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-228] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-178] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [138-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [172-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [177-186] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [188-202] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [206-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-61] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-178] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [130-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [180-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [205-229] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [233-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-219] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-216] for track '27' has 4 frames without a visible bounding box.
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