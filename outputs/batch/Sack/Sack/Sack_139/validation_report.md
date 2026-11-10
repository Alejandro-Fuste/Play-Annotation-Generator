# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_139`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_139/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [71-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-147] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [100-134] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [139-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-24] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [86-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [93-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-114] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-141] for track '22' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.