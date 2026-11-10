# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_76`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 11 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-48] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-141] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [117-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-64] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-78] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [107-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [133-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [148-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-146] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-151] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-196] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.