# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_202`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_202/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 406: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-104] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-152] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-170] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-95] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-131] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [63-79] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [81-107] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-175] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-129] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-175] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-175] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-60] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-94] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-102] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-17] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-175] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-16] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-175] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-146] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-155] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-175] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-175] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '31' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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