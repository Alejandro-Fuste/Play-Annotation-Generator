# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_225`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_225/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-51] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-62] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [93-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [112-149] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-133] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-82] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-141] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-100] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-150] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-150] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-139] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.