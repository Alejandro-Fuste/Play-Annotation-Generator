# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_184`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_184/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-83] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-93] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [65-92] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [96-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [107-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [111-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [118-119] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [91-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [97-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [106-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-120] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-108] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-83] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-83] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-91] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-108] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [106-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [110-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-91] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-108] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.