# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_80`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_CloseOnQuarterback' range [98-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-74] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [116-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [119-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [130-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [138-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [123-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.