# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_65`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [100-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [109-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [72-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [101-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-52] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-111] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-120] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-78] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '25' has 1 frames without a visible bounding box.
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