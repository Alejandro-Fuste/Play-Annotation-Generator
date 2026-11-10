# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_143`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_143/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-191] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [100-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [127-178] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-150] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-117] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [100-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [168-196] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [113-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [126-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-125] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-144] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-153] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [133-139] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [151-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-175] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-182] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-162] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-213] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-185] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-230] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-261] for track '33' has 2 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.