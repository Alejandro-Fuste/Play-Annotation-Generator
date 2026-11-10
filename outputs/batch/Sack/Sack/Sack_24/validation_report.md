# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_24`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-153] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [173-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [187-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [173-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [194-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [197-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [201-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [173-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [210-213] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [216-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-199] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '18' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.